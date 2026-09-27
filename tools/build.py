"""Package future Abyssal source as a deterministic Lumiverse format-3 archive."""

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLES = (
    "01-foundation.css",
    "02-shell.css",
    "03-chat.css",
    "04-adapters.css",
    "05-responsive.css",
)
OUTPUT = ROOT / "dist" / "abyssal-constellation.lumitheme"
URL = re.compile(r"url\(\s*(['\"]?)([^)'\"\s][^)'\"]*)\1\s*\)", re.I)
ARCHIVE_PATH = re.compile(r"^[A-Za-z0-9._/-]+$")
ZIP_DATE = (1980, 1, 1, 0, 0, 0)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read valid JSON from {path.relative_to(ROOT)}: {exc}") from exc


def safe_path(value, label):
    require(isinstance(value, str) and value, f"{label} must be a nonempty path")
    require(bool(ARCHIVE_PATH.fullmatch(value)), f"{label} has unsupported characters: {value}")
    require(".." not in value, f"{label} is rejected by Lumiverse: {value}")
    require(not value.startswith("/") and not value.startswith("./"), f"{label} is not relative: {value}")
    require(all(part not in ("", ".", "..") for part in value.split("/")), f"{label} is unsafe: {value}")
    require(not value.startswith("reference/") and not value.startswith("dist/"), f"{label} is forbidden: {value}")
    return value


def load_source():
    metadata = read_json(ROOT / "src" / "theme.json")
    require(isinstance(metadata, dict), "Source theme metadata must be an object")
    require("globalCSS" not in metadata and "assets" not in metadata, "Generated fields belong outside src/theme.json")
    require(metadata.get("format") == 3, "Lumiverse archive format must be 3")
    for key in ("name", "author", "description", "bundleId"):
        require(isinstance(metadata.get(key), str), f"Missing or invalid metadata: {key}")
    require(bool(metadata["name"]) and bool(metadata["bundleId"]), "Theme name and bundleId are required")
    require(bool(re.fullmatch(r"[A-Za-z0-9._-]{1,128}", metadata["bundleId"])), "Invalid bundleId")
    require(type(metadata.get("createdAt")) is int, "Missing or invalid metadata: createdAt")
    require(isinstance(metadata.get("theme"), dict), "Missing or invalid metadata: theme")
    require(isinstance(metadata.get("components"), dict), "Missing or invalid metadata: components")
    for name, component in metadata["components"].items():
        require(isinstance(name, str) and isinstance(component, dict), f"Invalid component: {name}")
        require(isinstance(component.get("css"), str) and isinstance(component.get("tsx"), str)
                and isinstance(component.get("enabled"), bool), f"Invalid component override: {name}")

    css_parts = []
    for name in STYLES:
        path = ROOT / "src" / "styles" / name
        try:
            css_parts.append(path.read_bytes().decode("utf-8"))
        except (OSError, UnicodeError) as exc:
            raise ValueError(f"Missing or invalid source CSS file: {path.relative_to(ROOT)}") from exc
    css = "".join(css_parts)
    require(len(css) <= 2_000_000, "CSS exceeds Lumiverse import limit")

    assets = read_json(ROOT / "src" / "assets.json")
    require(isinstance(assets, list), "Source asset manifest must be an array")
    slugs, destinations, files, manifest_assets = set(), {"theme.json"}, {}, []
    for index, asset in enumerate(assets):
        require(isinstance(asset, dict), f"Invalid asset at index {index}")
        slug = safe_path(asset.get("slug"), "Asset slug")
        destination = safe_path(asset.get("archivePath"), "Archive destination")
        source = safe_path(asset.get("source"), "Asset source")
        require(source.startswith("assets/") and destination.startswith("assets/")
                and slug.startswith("assets/"), f"Asset must be under assets/: {slug}")
        require(all(re.fullmatch(r"[a-z0-9][a-z0-9._-]*", part) for part in slug.split("/")),
                f"Asset slug would be renamed by Lumiverse: {slug}")
        require(slug not in slugs, f"Duplicate asset slug: {slug}")
        require(destination not in destinations, f"Duplicate archive destination: {destination}")
        slugs.add(slug)
        destinations.add(destination)
        for key in ("originalFilename", "mimeType"):
            require(isinstance(asset.get(key), str) and asset[key], f"Missing {key} for {slug}")
        require(isinstance(asset.get("tags"), list) and all(isinstance(tag, str) for tag in asset["tags"]),
                f"Invalid tags for {slug}")
        require(isinstance(asset.get("metadata"), dict), f"Invalid asset metadata for {slug}")
        path = ROOT / source
        require(path.resolve().is_relative_to((ROOT / "assets").resolve()),
                f"Asset source escapes assets/: {source}")
        require(path.is_file(), f"Missing declared asset: {source}")
        files[destination] = path.read_bytes()
        require(len(files[destination]) <= 50 * 1024 * 1024, f"Asset exceeds Lumiverse entry limit: {source}")
        manifest_assets.append({key: value for key, value in asset.items() if key != "source"})

    for match in URL.finditer(css):
        url = match.group(2).strip()
        if url.startswith(("http://", "https://", "data:", "blob:", "/", "#")):
            continue
        normalized = url.removeprefix("./")
        require(normalized in slugs, f"Unresolved local CSS asset URL: {url}")

    manifest = {**{key: value for key, value in metadata.items() if key != "components"},
                "globalCSS": css, "components": metadata["components"], "assets": manifest_assets}
    files["theme.json"] = json.dumps(manifest, ensure_ascii=False, indent=2).encode("utf-8")
    require(len(files) <= 500, "Archive exceeds Lumiverse entry limit")
    require(len(files["theme.json"]) <= 50 * 1024 * 1024, "Theme manifest exceeds Lumiverse entry limit")
    require(sum(len(data) for data in files.values()) <= 250 * 1024 * 1024,
            "Archive expands beyond Lumiverse import limit")
    return manifest, files


def write_archive(files):
    OUTPUT.parent.mkdir(exist_ok=True)
    temp = OUTPUT.with_suffix(".tmp")
    with zipfile.ZipFile(temp, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for name in ("theme.json", *(key for key in files if key != "theme.json")):
            info = zipfile.ZipInfo(name, ZIP_DATE)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, files[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=6)
    temp.replace(OUTPUT)
    require(OUTPUT.stat().st_size <= 200 * 1024 * 1024, "Archive exceeds Lumiverse import limit")
    with zipfile.ZipFile(OUTPUT) as archive:
        require(set(archive.namelist()) == set(files) and len(archive.namelist()) == len(files),
                "Archive contains unexpected or missing files")
        require(all(not name.startswith("reference/") for name in archive.namelist()),
                "Archive contains reference files")
        require(all(archive.read(name) == data for name, data in files.items()),
                "Archive content differs from source")


def main():
    require((ROOT / "src").is_dir(),
            "Theme source has not been initialized yet. Create src/ during the next implementation milestone.")
    manifest, files = load_source()
    write_archive(files)
    print(f"Built {OUTPUT.relative_to(ROOT)}: {len(manifest['globalCSS'].encode('utf-8'))} CSS bytes, "
          f"{len(manifest['assets'])} assets, {len(files)} archive members")


def self_test():
    """Exercise the real CLI in a temporary source tree, without local references."""
    with tempfile.TemporaryDirectory(prefix="abyssal-packer-") as temporary:
        fixture = Path(temporary)
        (fixture / "tools").mkdir()
        (fixture / "src" / "styles").mkdir(parents=True)
        (fixture / "assets").mkdir()
        shutil.copyfile(__file__, fixture / "tools" / "build.py")

        metadata = {
            "format": 3, "name": "Packaging self-test", "author": "", "description": "",
            "createdAt": 0, "bundleId": "packaging-self-test", "theme": {}, "components": {},
        }
        assets = [{
            "slug": "assets/sample.svg", "originalFilename": "sample.svg",
            "mimeType": "image/svg+xml", "tags": [], "metadata": {},
            "archivePath": "assets/001-sample.svg", "source": "assets/sample.svg",
        }]
        asset_bytes = b'<svg xmlns="http://www.w3.org/2000/svg"/>'
        (fixture / "src" / "theme.json").write_text(json.dumps(metadata), encoding="utf-8")
        (fixture / "src" / "assets.json").write_text(json.dumps(assets), encoding="utf-8")
        (fixture / "assets" / "sample.svg").write_bytes(asset_bytes)
        for name in STYLES:
            css = '.fixture { background: url("assets/sample.svg"); }\n' if name == STYLES[0] else ""
            (fixture / "src" / "styles" / name).write_text(css, encoding="utf-8")

        command = [sys.executable, str(fixture / "tools" / "build.py")]
        def run_build():
            return subprocess.run(command, cwd=fixture, stdin=subprocess.DEVNULL,
                                  capture_output=True, text=True, check=False)

        first = run_build()
        require(first.returncode == 0, f"Self-test build failed: {first.stderr}")
        archive_path = fixture / "dist" / OUTPUT.name
        first_hash = hashlib.sha256(archive_path.read_bytes()).digest()
        second = run_build()
        require(second.returncode == 0, f"Self-test repeat build failed: {second.stderr}")
        require(hashlib.sha256(archive_path.read_bytes()).digest() == first_hash,
                "Self-test archive changed between identical builds")
        with zipfile.ZipFile(archive_path) as archive:
            require(archive.namelist() == ["theme.json", "assets/001-sample.svg"],
                    "Self-test archive contains unexpected members")
            require(archive.testzip() is None and archive.read("assets/001-sample.svg") == asset_bytes,
                    "Self-test asset failed archive validation")
            manifest = json.loads(archive.read("theme.json"))
            require(manifest["format"] == 3 and manifest["assets"][0]["slug"] == "assets/sample.svg",
                    "Self-test manifest or asset slug is invalid")

        (fixture / "src" / "styles" / STYLES[0]).write_text(
            '.fixture { background: url("assets/missing.svg"); }\n', encoding="utf-8")
        invalid = run_build()
        require(invalid.returncode != 0 and "Unresolved local CSS asset URL" in invalid.stderr,
                "Self-test did not reject an unresolved local CSS asset URL")
    print("Packaging self-test passed: valid archive, asset resolution, validation, reproducible ZIP")


if __name__ == "__main__":
    try:
        if sys.argv[1:] == ["--self-test"]:
            self_test()
        elif not sys.argv[1:]:
            main()
        else:
            raise ValueError("Usage: python tools/build.py [--self-test]")
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        sys.exit(1)
