# Abyssal Constellation Rebuild Roadmap

## Project Goal

Rebuild the adopted Abyssal Constellation theme as a clean, maintainable, lightweight, CSS-first Lumiverse theme. Preserve Lunch's original visual identity, the current Abyssal palette and assets, and Lumiverse-specific behavior. Use Honeyed Twilight for architectural direction and Moonlit Echoes for Echo-style message composition and visual language, without carrying over SillyTavern-specific implementation details.

Abyssal is the Lumiverse implementation and visual reference; Honeyed Twilight is the architectural reference; Moonlit Echoes is the visual and composition reference. The current Abyssal CSS remains only under `reference/` and is not the new source architecture. Prefer semantic Lumiverse hooks such as `data-component` and `data-part` over generated class names. Historical Vxx patch layers do not enter `src/`; preserve or intentionally replace their visual behavior as the clean implementation is built.

### Target Chat Experience

- Desktop uses Moonlit Echoes Echo as the primary composition reference.
- Mobile uses Moonlit Echoes Whisper as the primary composition reference.
- Tablet intentionally transitions between Echo-like and Whisper-like composition based on available width, rather than simply shrinking the desktop layout.
- Reproduce these visual behaviors natively in Lumiverse with one shared Abyssal design system.
- Share the underlying tokens, message primitives, author-role semantics, metadata system, and artwork system across breakpoints. Responsive composition may change significantly while the design system stays unified.

## Milestone 0 — Audit

**Status:** Complete

The initial audit established the repository state, the monolithic Abyssal theme structure, its technical debt, available semantic hooks and fragile generated-class selectors. It identified Abyssal traits to preserve, Honeyed architectural patterns, Moonlit Echo composition patterns, a clean source structure, and the ordered rebuild strategy. Subsequent format verification confirmed that CSS URLs resolve through asset slugs, which map to numbered archive members. The absence of a build pipeline was the baseline issue.

## Milestone 1 — Reproducible Baseline

**Goal:** Validate and establish the packaging/tooling foundation before implementation.

**Historical work:** Inspected the original bundle and Lumiverse import/export code, adopted the original artwork at clean source paths, verified asset slug/archive mappings, and proved deterministic packaging against a temporary legacy extraction. That extraction was discarded; current production source is independent of the reference bundle.

**Done when:** The packaging self-test builds a valid deterministic format-3 archive without `reference/`, and `reference/` and `dist/` remain ignored.

**Packaging proof:** The temporary legacy extraction once produced a byte-identical manifest and payload. That historical comparison is complete. `tools/build.py --self-test` now checks archive validity, asset resolution, CSS validation, and deterministic output with disposable fixtures.

## Milestone 2 — Foundation & Native Lumiverse Integration

**Status:** Complete

**Goal:** Establish the Abyssal identity through native Lumiverse theme configuration and a minimal custom CSS foundation.

**Scope:** A coherent v46-based `ThemeConfig` drives Lumiverse's native palette generation and live Accent, Primary, and Background customization. Native glass behavior and wallpaper compatibility remain intact. The bundled identity font is available for later character styling; `base.css` adds the custom selection treatment. Navigation, drawers, modals, forms, InputArea, scrollbars, and other app shell elements use native Lumiverse styling unless a future visual requirement justifies an override. Packaging is deterministic and includes only referenced assets.

**Done when:** The format-3 theme builds reproducibly, native theme controls work, wallpaper remains compatible, and no redundant app shell CSS is required. Chat presentation belongs to later milestones.

## Milestone 3 — Unified Responsive Chat System

**Goal:** Build one shared, parameterized Abyssal message system that produces Echo-inspired composition on desktop and Whisper-inspired composition on mobile.

### Responsive Design Intent

- Desktop composition: Echo.
- Mobile composition: Whisper.
- Tablet composition: an intentional intermediate based on available width.
- Share tokens and message primitives across desktop, tablet, and mobile; user and character roles remain part of one system.
- Whisper on mobile is a responsive composition of the shared theme, not a separate theme.
- BubbleMessage and MinimalMessage consume the same visual model.

**Tasks:** Define shared message primitives and geometry variables; compose character and user messages with intentional asymmetry; integrate artwork/avatars while reserving readable content space; style names, quiet metadata, actions, swipe/regeneration controls, streaming, greetings, and system messages.

**Requirement:** The visual design exists once. BubbleMessage and MinimalMessage must not become separate themes; leave their DOM differences to adapters.

**Done when:** Both roles share one recognizable Abyssal design system with Echo-inspired desktop and Whisper-inspired mobile composition, integrated artwork, subdued metadata, and no duplicate full message implementations.

## Milestone 4 — Bubble & Minimal Adapters

**Goal:** Map the shared design onto Lumiverse's BubbleMessage and MinimalMessage DOM structures.

**Tasks:** Add thin BubbleMessage and MinimalMessage adapters for MessageContent, actions, role, streaming, and greeting mappings. Use fallbacks only where semantic hooks are unavailable.

**Rules:** Adapters bridge DOM differences only; design values stay shared. Prefer `data-component` and `data-part`, and document every retained generated-class fallback.

**Done when:** Both modes look like the same theme, consume shared tokens and geometry, have minimal documented generated-class dependencies, and avoid page-wide mode inference where possible.

## Milestone 5 — Responsive & Edge Cases

**Goal:** Make the chat system reliable without breakpoint patch stacking.

**Responsive model:** Desktop uses Echo-style composition; tablet uses a deliberate transitional composition based on width and content constraints; mobile uses Whisper-style composition. Add a small-phone override only where evidence requires it.

**Principle:** Responsive behavior is a composition change, not merely desktop CSS compressed into a smaller viewport.

**Test cases:** Long roleplay and short messages; long names and multiline metadata; large and small portraits; streaming, swipes, regeneration, greetings, system messages, and empty states; tablet and mobile portrait orientation; expanding chat input.

**Done when:** Echo and Whisper layouts have no known overflow or clipping; artwork scales predictably; text stays readable; actions remain usable; and there are no chains of breakpoint-specific fixes.

## Milestone 6 — Chat Implementation Debt Review

**Goal:** Review the completed chat implementation for obsolete fallbacks and avoid new patch layers.

**Tasks:** Audit chat selectors, cascade order, responsive geometry, and intentional compatibility fallbacks. Remove dead or superseded rules introduced during chat work. Minimize `!important`, `:has()`, and generated-class selectors where semantic hooks exist.

**Track before and after:** CSS lines and bytes, rule blocks, `!important`, `:has()`, generated-class selector counts, and semantic hook usage. Metrics diagnose debt; they are not optimization targets.

**Done when:** Chat source has no known dead rules, and every remaining fallback or fragile selector has a current reason.

## Milestone 7 — Visual Parity & Polish

**Goal:** Refine the completed theme against all three references.

**Abyssal:** Preserve the palette, constellation atmosphere, moon artwork, navy/near-black glass, blue interaction accents, pale-gold identity, and softly faded portraits.

**Honeyed:** Preserve a clean cascade, Lumiverse-native behavior, and maintainable structure.

**Moonlit Echoes:** Refine Echo-style desktop and Whisper-style mobile composition, integrated artwork, restrained chrome, quiet metadata, generous spacing, translucent message surfaces, and glass input treatment. Future palette analysis should inspect both Echo and Whisper, since their readability and surface treatment may differ.

**Tasks:** Compare side-by-side desktop, tablet, and mobile screenshots; make a visual consistency and accessibility/readability pass; polish spacing and typography.

**Done when:** The result is unmistakably Abyssal Constellation, achieves the intended Moonlit Echoes-inspired message feel, and remains cleaner than the original implementation.

## Milestone 8 — v1.0 Release

**Goal:** Ship the first clean rebuilt release.

**Tasks:** Produce a production `.lumitheme`; test fresh import, asset resolution, and import/export round-trip where supported; update the README with installation and build instructions, screenshots, credits, attribution, version metadata, and changelog/release notes; prepare the GitHub release.

**Done when:** Fresh installation works, no local/reference files or broken assets are packaged, the repository and documentation are current, and the v1.0.0 artifact is reproducible.

## Engineering Principles

1. Build behavior, not history.
2. One shared message system may have different responsive compositions; variants reuse semantic roles, tokens, artwork model, metadata system, and adapters.
3. Semantic Lumiverse selectors first.
4. Generated classes only as documented fallbacks.
5. CSS-first.
6. Preserve Lumiverse geometry unless overriding it is intentional.
7. One authoritative declaration per property and state where practical.
8. No patch-on-patch development.
9. Keep legacy reference CSS outside `src/`; add only rules justified by current behavior.
10. Maintainability matters more than minimizing line count.
11. Keep every milestone buildable and reviewable.
12. Do not modify files under `reference/`.

## Milestone Status

- [x] Milestone 0 — Audit
- [x] Milestone 1 — Reproducible Baseline
- [x] Milestone 2 — Foundation & Native Lumiverse Integration
- [ ] Milestone 3 — Unified Echo-Inspired Chat System
- [ ] Milestone 4 — Bubble & Minimal Adapters
- [ ] Milestone 5 — Responsive & Edge Cases
- [ ] Milestone 6 — Chat Implementation Debt Review
- [ ] Milestone 7 — Visual Parity & Polish
- [ ] Milestone 8 — v1.0 Release
