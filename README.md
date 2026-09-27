# Abyssal Constellation Theme for Lumiverse

A dark, atmospheric theme for [Lumiverse](https://github.com/prolix-oc/Lumiverse), inspired by deep-space colors, translucent UI elements, character-focused chat layouts, and the visual style of Moonlit Echoes.

## Credits

The original **Abyssal Constellation** theme was created by **Lunch**.

This repository is an adopted and maintained version of the theme, with the goal of improving compatibility, maintainability, responsiveness, and overall integration with modern Lumiverse releases while preserving the original visual identity.

## Goals

- Preserve the original Abyssal Constellation aesthetic
- Improve Lumiverse compatibility
- Reduce accumulated CSS technical debt
- Improve desktop, tablet, and mobile layouts
- Use stable Lumiverse component selectors where possible
- Refine the chat experience toward the visual language of Moonlit Echoes
- Keep the theme easy to maintain as Lumiverse evolves

## Installation

Download the latest `.lumitheme` release and import it through Lumiverse's theme manager.

## Development

Python 3.10 or newer is required; no packages need installing. `assets/` contains adopted Abyssal artwork. `tools/build.py` is the production packaging path, and `tools/compare_baseline.py` is an optional local reference comparison aid. `reference/` is ignored and contains the old theme for visual, behavioral, and selector research; it is never a build input.

There is no `src/` yet and no production theme can currently be built. The next implementation milestone will create each new source file from scratch. For now, `python tools/build.py` reports that theme source has not been initialized. Run `python tools/build.py --self-test` to validate packaging, asset resolution, and reproducible ZIP output using temporary fixtures. The self-test does not create repository source or a release artifact.

When a built archive exists later, `python tools/compare_baseline.py` can report differences against the local reference bundle. It reports clearly when the optional reference is unavailable.

The project takes inspiration from:

- The original **Abyssal Constellation** theme by Lunch
- **Honeyed Twilight** for cleaner Lumiverse-native theme architecture
- **Moonlit Echoes** for chat presentation and visual direction

## Credits & Attribution

Original Abyssal Constellation theme: **Lunch**

Lumiverse adaptation and maintenance: **cLonata**

All credit for the original theme concept and design belongs to its original creator.
