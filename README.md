# Abyssal Constellation for Lumiverse

A dark, atmospheric [Lumiverse](https://github.com/prolix-oc/Lumiverse) theme. The original Abyssal Constellation was created by **Lunch**; this adaptation is maintained by **cLonata**.

## Status

The `staging` branch is in active development. The native Lumiverse foundation is buildable; Echo and Whisper chat presentation is still planned.

## Installation

Build locally, then import `dist/abyssal-constellation.lumitheme` through Lumiverse's theme manager. There is no published release yet.

## Development

Python 3.10 or newer is required. No extra packages are needed.

```sh
python tools/build.py
python tools/build.py --self-test
```

`src/theme.json` holds the native theme configuration; `src/styles/` holds the small custom CSS foundation; `src/assets.json` lists bundled assets. `assets/` also retains artwork for future work. The local, ignored `reference/` directory is for research and is never a build input.
