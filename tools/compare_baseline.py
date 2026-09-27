"""Report differences from the local, ignored Abyssal reference bundle."""

import hashlib
import json
import sys
import zipfile

from build import OUTPUT, ROOT


REFERENCE = ROOT / "reference" / "Abyssal Constellation"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def differences(original, generated, prefix=""):
    if isinstance(original, dict) and isinstance(generated, dict):
        result = {}
        for key in sorted(original.keys() | generated.keys()):
            result.update(differences(original.get(key), generated.get(key), f"{prefix}{key}."))
        return result
    if original == generated:
        return {}
    return {prefix[:-1]: {"reference": original, "built": generated}}


def main(strict=False):
    reference_manifest = REFERENCE / "theme.json"
    if not reference_manifest.is_file():
        raise FileNotFoundError(f"Optional local baseline unavailable: {reference_manifest}")
    if not OUTPUT.is_file():
        raise FileNotFoundError(f"No built archive to compare: {OUTPUT}. Production source is not initialized yet.")

    original_bytes = reference_manifest.read_bytes()
    original = json.loads(original_bytes)
    with zipfile.ZipFile(OUTPUT) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise ValueError(f"Archive CRC failed: {bad_member}")
        names = archive.namelist()
        generated_bytes = archive.read("theme.json")
        generated = json.loads(generated_bytes)
        expected_generated_names = {"theme.json", *(asset["archivePath"] for asset in generated["assets"])}
        if set(names) != expected_generated_names or len(names) != len(expected_generated_names):
            raise ValueError("Archive member set differs from its own manifest")

        metadata_keys = (set(original) | set(generated)) - {"globalCSS", "assets"}
        metadata_differences = differences(
            {key: original.get(key) for key in metadata_keys},
            {key: generated.get(key) for key in metadata_keys},
        )
        print("Metadata differences:", metadata_differences)
        print("Manifest byte-identical:", original_bytes == generated_bytes)

        old_css, new_css = original["globalCSS"], generated["globalCSS"]
        print("CSS lines (reference / built):", len(old_css.splitlines()), len(new_css.splitlines()))
        print("CSS bytes (reference / built):", len(old_css.encode()), len(new_css.encode()))
        print("CSS byte-identical:", old_css == new_css)

        old_assets = {asset["slug"]: asset for asset in original["assets"]}
        new_assets = {asset["slug"]: asset for asset in generated["assets"]}
        print("Asset counts (reference / built):", len(old_assets), len(new_assets))
        print("Removed asset slugs:", sorted(old_assets.keys() - new_assets.keys()))
        print("Added asset slugs:", sorted(new_assets.keys() - old_assets.keys()))
        assets_match = old_assets.keys() <= new_assets.keys()
        for slug in sorted(old_assets.keys() & new_assets.keys()):
            old, new = old_assets[slug], new_assets[slug]
            old_hash = digest((REFERENCE / old["archivePath"]).read_bytes())
            new_hash = digest(archive.read(new["archivePath"]))
            metadata_match = old == new
            print(f"{slug}: SHA-256 {new_hash}; bytes match={old_hash == new_hash}; "
                  f"manifest entry match={metadata_match}")
            assets_match &= old_hash == new_hash and metadata_match

        reference_names = {"theme.json", *(asset["archivePath"] for asset in original["assets"])}
        print("Archive members removed:", sorted(reference_names - set(names)))
        print("Archive members added:", sorted(set(names) - reference_names))
        if not assets_match:
            raise ValueError("An adopted reference asset is missing or changed")
        if strict and (metadata_differences or original_bytes != generated_bytes or old_css != new_css
                       or old_assets.keys() != new_assets.keys() or reference_names != set(names)):
            raise ValueError("Strict reference parity failed; the clean rebuild is expected to differ")
    print("Adopted asset comparison passed; CSS differences are expected during the rebuild")


if __name__ == "__main__":
    try:
        if any(arg != "--strict" for arg in sys.argv[1:]):
            raise ValueError("Usage: python tools/compare_baseline.py [--strict]")
        main(strict="--strict" in sys.argv[1:])
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as exc:
        print(f"Baseline comparison failed: {exc}", file=sys.stderr)
        sys.exit(1)
