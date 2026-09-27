# Abyssal Constellation Rebuild Roadmap

## Project Goal

Rebuild the adopted Abyssal Constellation theme as a clean, maintainable, lightweight, CSS-first Lumiverse theme. Preserve Lunch's original visual identity, the current Abyssal palette and assets, and Lumiverse-specific behavior. Use Honeyed Twilight for architectural direction and Moonlit Echoes for Echo-style message composition and visual language, without carrying over SillyTavern-specific implementation details.

Abyssal is the Lumiverse implementation and visual reference; Honeyed Twilight is the architectural reference; Moonlit Echoes is the visual and composition reference. The current Abyssal CSS is not the architecture to preserve. Prefer semantic Lumiverse hooks such as `data-component` and `data-part` over generated class names. Historical Vxx patch layers should disappear, but preserve or intentionally replace each visual behavior before removing its legacy rule.

## Milestone 0 — Audit

**Status:** Complete

The initial audit established the repository state, the monolithic Abyssal theme structure, its technical debt, available semantic hooks and fragile generated-class selectors. It identified Abyssal traits to preserve, Honeyed architectural patterns, Moonlit Echo composition patterns, a clean source structure, and the ordered rebuild strategy. Asset path mismatches and the absence of a build pipeline are known baseline issues.

## Milestone 1 — Reproducible Baseline

**Goal:** Turn the monolithic reference bundle into editable source and a deterministic build without intentionally changing its appearance.

**Tasks:** Create source theme metadata; split `globalCSS` into ordered source CSS files; extract assets to clean source paths and verify slug/archive mappings; add lightweight packaging tooling; build a valid `.lumitheme` in `dist/`. Validate missing assets and duplicate slugs, exclude `reference/` from output, document the build command, and compare generated output with the Abyssal reference for semantic parity.

**Done when:** One command builds a valid theme from editable source; assets resolve; the current cascade and visual behavior are preserved; no redesign has begun; generated output is semantically equivalent to the reference; `reference/` and `dist/` remain uncommitted.

## Milestone 2 — Foundation & Lumiverse Shell

**Goal:** Replace legacy app-shell styling with a clean Honeyed-inspired foundation while leaving chat presentation functionally unchanged.

**Tasks:** Establish tokens for palette, typography, spacing, glass, blur, borders, shadows, motion, and backgrounds. Rebuild navigation/header, sidebars/drawers, cards/panels, dialogs/modals, forms and input controls, chat input, scrollbars, and minor chrome.

**Rules:** Let Lumiverse manage layout geometry where possible. Prefer semantic hooks; use generated-class selectors and `!important` only when needed. Do not redesign message layout yet.

**Done when:** The shell has a clear structure, no historical Vxx shell patches, no obvious app-chrome regressions, and working baseline chat.

## Milestone 3 — Unified Echo-Inspired Chat System

**Goal:** Build one shared, parameterized message design inspired by Moonlit Echoes' Echo style.

**Tasks:** Define shared message primitives and geometry variables; compose character and user messages with intentional asymmetry; integrate artwork/avatars while reserving readable content space; style names, quiet metadata, actions, swipe/regeneration controls, streaming, greetings, and system messages.

**Requirement:** The visual design exists once. BubbleMessage and MinimalMessage must not become separate themes; leave their DOM differences to adapters.

**Done when:** Both roles share one recognizable Abyssal design system with Moonlit Echo influence, integrated artwork, subdued metadata, and no duplicate full message implementations.

## Milestone 4 — Bubble & Minimal Adapters

**Goal:** Map the shared design onto Lumiverse's BubbleMessage and MinimalMessage DOM structures.

**Tasks:** Add thin BubbleMessage and MinimalMessage adapters for MessageContent, actions, role, streaming, and greeting mappings. Use fallbacks only where semantic hooks are unavailable.

**Rules:** Adapters bridge DOM differences only; design values stay shared. Prefer `data-component` and `data-part`, and document every retained generated-class fallback.

**Done when:** Both modes look like the same theme, consume shared tokens and geometry, have minimal documented generated-class dependencies, and avoid page-wide mode inference where possible.

## Milestone 5 — Responsive & Edge Cases

**Goal:** Make the chat system reliable without breakpoint patch stacking.

**Responsive model:** Desktop by default; tablet near 1100px; mobile near 760–820px; add a small-phone override only when evidence requires it.

**Test cases:** Long roleplay and short messages; long names and multiline metadata; large and small portraits; streaming, swipes, regeneration, greetings, system messages, and empty states; tablet and mobile portrait orientation; expanding chat input.

**Done when:** No known overflow or clipping remains, artwork scales predictably, text stays readable, actions remain usable, and there are no chains of breakpoint-specific fixes.

## Milestone 6 — Legacy Debt Purge

**Goal:** Remove old implementation only after its replacement behavior is proven.

**Tasks:** Remove Vxx sections, superseded and dead rules, duplicate selectors, and obsolete compatibility rules. Reduce unnecessary `!important` and `:has()`, replace fragile selectors where semantic hooks exist, consolidate repeated values, and audit geometry and cascade order.

**Track before and after:** CSS lines and bytes; rule blocks; `!important`, `:has()`, and generated-class selector counts; semantic hook usage; repeated selector count. Metrics diagnose debt, but are not optimization targets.

**Done when:** No historical Vxx sections or known obsolete rules remain; source makes sense without theme history; every remaining `!important` and generated-class selector is intentional. Clarity takes priority over line count.

## Milestone 7 — Visual Parity & Polish

**Goal:** Refine the completed theme against all three references.

**Abyssal:** Preserve the palette, constellation atmosphere, moon artwork, navy/near-black glass, blue interaction accents, pale-gold identity, and softly faded portraits.

**Honeyed:** Preserve a clean cascade, Lumiverse-native behavior, and maintainable structure.

**Moonlit Echoes:** Refine Echo-style composition, integrated artwork, restrained chrome, quiet metadata, generous spacing, translucent message surfaces, and glass input treatment.

**Tasks:** Compare side-by-side desktop, tablet, and mobile screenshots; make a visual consistency and accessibility/readability pass; polish spacing and typography.

**Done when:** The result is unmistakably Abyssal Constellation, achieves the intended Moonlit Echoes-inspired message feel, and remains cleaner than the original implementation.

## Milestone 8 — v1.0 Release

**Goal:** Ship the first clean rebuilt release.

**Tasks:** Produce a production `.lumitheme`; test fresh import, asset resolution, and import/export round-trip where supported; update the README with installation and build instructions, screenshots, credits, attribution, version metadata, and changelog/release notes; prepare the GitHub release.

**Done when:** Fresh installation works, no local/reference files or broken assets are packaged, the repository and documentation are current, and the v1.0.0 artifact is reproducible.

## Engineering Principles

1. Build behavior, not history.
2. One visual system, thin adapters.
3. Semantic Lumiverse selectors first.
4. Generated classes only as documented fallbacks.
5. CSS-first.
6. Preserve Lumiverse geometry unless overriding it is intentional.
7. One authoritative declaration per property and state where practical.
8. No patch-on-patch development.
9. Remove each legacy rule only after replacement behavior exists.
10. Maintainability matters more than minimizing line count.
11. Keep every milestone buildable and reviewable.
12. Do not modify files under `reference/`.

## Milestone Status

- [x] Milestone 0 — Audit
- [ ] Milestone 1 — Reproducible Baseline
- [ ] Milestone 2 — Foundation & Lumiverse Shell
- [ ] Milestone 3 — Unified Echo-Inspired Chat System
- [ ] Milestone 4 — Bubble & Minimal Adapters
- [ ] Milestone 5 — Responsive & Edge Cases
- [ ] Milestone 6 — Legacy Debt Purge
- [ ] Milestone 7 — Visual Parity & Polish
- [ ] Milestone 8 — v1.0 Release
