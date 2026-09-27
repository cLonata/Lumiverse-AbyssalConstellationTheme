# Color Palette Audit

## 1. Methodology

This audit compares the bundled Abyssal and Honeyed `theme.json` files with Moonlit Echoes' CSS, color settings, inline CSS, and three local presets. For the Lumiverse bundles, `globalCSS` line numbers below refer to the **decoded CSS string**, not physical JSON lines. The literal inventory in the appendix records each distinct source spelling, its first source, a likely role, and its normalized color. `#rrggbb / a` means that base RGB color at alpha `a`; HSL conversions are rounded to the nearest 8-bit channel.

Counted sources: `reference/Abyssal Constellation/theme.json`; `reference/Honeyed Twilight/theme.json`; `reference/Moonlit Echoes/style.css`, `extension.css`, `src/ui/settings-factory.css`, `src/config/theme-settings.js`, `src/ui/settings-factory.js`, and all three JSON files in `theme/`. The other Moonlit JS files were searched for color declarations; `src/utils/color.js` contains generic conversion fallbacks, not preset colors. The Honeyed bundle has no separate component CSS in the local reference, despite a comment pointing to one.

Counts cover explicit hex, RGB(A), and HSL(A) paint literals in those sources, including visible gradient stops and JSON metadata. They exclude `transparent`, `currentColor`, alpha-zero stops, mask-only stops, the inactive Abyssal `#080812` fallback for `--lumiverse-bg`, and Moonlit's white color-picker fallback. CSS `color-mix()` and external runtime variables are described but do not add fabricated literal colors to the counts. The PNG artwork is assessed visually; its pixels are not counted as CSS literals. The SVG artwork is noted separately because hundreds of repeated star fills would distort UI frequency.

## 2. Abyssal Constellation

The main palette is blue-black with cool text and blue interaction color. Gold is concentrated in character names and their small star treatment. The root tokens and the later Bubble/Minimal overrides show both the intended identity and the competing historical values. Sources: `reference/Abyssal Constellation/theme.json` (`globalCSS` lines 3–53, 729–771, 878–925, 1658–1685, 1709–1765) and its `theme.baseColorsByMode.dark` / `theme.statusColors` fields.

| Role | Current source value → normalized value | Notes |
| --- | --- | --- |
| Root / deep background | `#030a15`, `#01040b` | Root, chat backdrop, and deep navy. |
| Raised panel | `#08162a`; `rgb(10 28 52 / 84%)` → `#0a1c34 / .84` | Existing Lumiverse elevated/fill tokens. |
| Glass | `rgb(6 19 38 / 88%)` → `#061326 / .88` | `--lcs-glass-bg`; current blur tokens are `0px`. |
| Bubble message | `rgb(4 15 31 / 96%)` → `#040f1f / .96`; `rgb(2 10 23 / 98%)` → `#020a17 / .98` | Final Bubble gradient, with blue radial haze. |
| Minimal message | `rgb(4 15 31 / 82%)` → `#040f1f / .82`; `rgb(3 12 27 / 76%)` → `#030c1b / .76` | Later content-glass gradient; the same base hue also appears at `.64`. |
| Main / secondary text | `#e7effb`, `#a8b8cd`, `#7f93ac`, `#61758f` | Pale blue-white to hint text. Prose dialogue is `#91b5df`. |
| Gold | `#e8cf91`; name gradients from `#cda95e` through `#fff1c8` to `#b99149` | Bubble and Minimal use similar, separately authored gold ramps. Gold glow uses low-alpha warm RGB. |
| Blue / cool highlight | `#587eaf`, `#6d91c3`, `#83afe0`, `#91b5df` | Primary, hover/secondary, prose link, and dialogue. A distinct cyan base is not established. |
| Borders | `rgb(82 119 163 / 30%)` → `#5277a3 / .30`; `rgb(109 145 195 / 48%)` → `#6d91c3 / .48` | Bubble edge later uses `#6d91c3 / .14`. |
| Hover / focus | `#6d91c3`; focused search border `rgb(145 181 223 / 34%)` → `#91b5df / .34` | Several hover states add translucent navy and blue. |
| Shadows / glow | Black at roughly `.12`–`.54`; white at `.018`–`.08`; warm gold at `.13`–`.54` | Dark depth, fine glass edges, and restrained name glow. |
| Status | `#c66b78` danger, `#559b96` success, `#c79b5d` warning | Duplicated in `statusColors` and dark base colors. |

**Artwork:** `reference/Abyssal Constellation/assets/001-abyssal-constellation.svg:3–16` uses sky stops `#01040b`, `#031020`, `#01050d` and translucent haze `#102b50 / .34`, `#0a1e3b / .18`, `#0c2446 / .28`, `#07162e / .13`. Star fills repeatedly use `#eef6ff`, `#c7daf2`, `#8fafd4`, and `#5f82ad`. The bundled PNG adds a blue moon and nebula field. Asset paths requested by the current CSS do not match its manifest, so live rendering must confirm which artwork currently appears.

**Token candidates and debt:** Root `--lumiverse-*` colors, `--lcs-glass-*`, the blue border pair, and the gold name ramp are strong candidates. The same navy/blue families recur as literals with many alpha values. `--ink`, `--muted`, `--line`, `--accent-soft`, and `--accent-warm` are defined twice with different values; the early purple `#b58bff / .30` and orange `#ff8154 / .25` treatments are later replaced by blue and should be treated as legacy candidates. Metadata lists primary `#0b72ff`, while `globalCSS` sets `--lumiverse-primary: #587eaf`; computed precedence needs a live check.

## 3. Honeyed Twilight

Honeyed uses warm near-black/brown surfaces, amber as its primary accent, and a clear token block. Sources: `reference/Honeyed Twilight/theme.json` (`globalCSS` lines 26–117, 261–310, 351–428) and `theme.baseColorsByMode.dark`.

| Role | Source value → normalized value | Notes |
| --- | --- | --- |
| Root / panel | `#1a1410`; `hsla(26, 28%, 8%, 0.55)` → `#1a140f / .55` | Dark warm base and reusable glass tint. |
| Drawer / modal | `#1a140f / .65`; `hsla(30, 35%, 10%, .85)` → `#221a11 / .85` | Related warm hues with role-specific opacity. |
| Text / muted | `#e8dcca`; `#9e8668` | Base text and thoughts. |
| Accent | `#c4943a`; `#d4a246` speech | No comparable blue interaction hue in this preset. |
| Border | `hsla(36, 40%, 40%, .15)` → `#8f6e3d / .15` | Shared by modal, message-card, and input border tokens. |
| Hover / active | `hsla(26, 28%, 15%, .50)` → `#31251c / .50`; `hsla(26, 28%, 18%, .60)` → `#3b2c21 / .60` | Settings navigation states. |
| Input | `#1a140f / .55` | Same glass family as the panel, assigned through `--ht-input-bg`. |
| Shadows | `#000000 / .12`, `#000000 / .20` | Light depth for message surfaces. |
| Status | `#d94848` danger, `#4aad5c` success, `#d4992e` warning | Theme JSON colors. |

The reusable structure is the lesson: `--ht-accent` resolves through `--lumiverse-primary` to a fallback, while message, quote, code, link, scrollbar, and selection variants derive from it with `color-mix()` (`globalCSS` lines 64–115). Nine distinct amber mix percentages serve separate roles without nine independently chosen hues. Surface tokens likewise stay grouped by purpose. The local bundle does **not** provide its referenced BubbleMessage component CSS, so actual Honeyed message fill cannot be mapped confidently. Its colors are architectural examples, not proposed Abyssal colors.

## 4. Moonlit Echoes

The canonical `Moonlit Echoes - by Rivelle` preset supplies the most useful comparison. The two Glimmer files are alternate looks and are included in counts, but their changed neutral colors should not be mistaken for the canonical Echo palette. Sources: `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:1–15`, `reference/Moonlit Echoes/src/config/theme-settings.js:37–99`, and `reference/Moonlit Echoes/style.css:1353–1580,2303–2371`.

| Role | Canonical/default value → normalized value | Notes |
| --- | --- | --- |
| App / panel | `rgba(33, 33, 33, .65)` → `#212121 / .65` blur tint | The chat backdrop is transparent over a user-selected image; there is no fixed navy background to port. |
| Echo user message | `rgba(45, 45, 45, .5)` → `#2d2d2d / .5` | `--SmartThemeUserMesBlurTintColor` in Echo user text. |
| Echo character message | `rgba(39, 39, 39, .65)` → `#272727 / .65` | `--SmartThemeBotMesBlurTintColor`; slightly darker and more opaque. |
| Main / muted text | `#cccccc`; italic `#969696` | Metadata also quiets through size and opacity in CSS. |
| Gold / warm | `rgba(250, 198, 121, 1)` → `#fac679` | Secondary setting and canonical underline color. |
| Blue / cyan | `rgba(81, 160, 222, 1)` → `#51a0de` | Primary interaction and quote color. |
| Borders | Canonical preset border is transparent; input border derives from body text at 60%, then 80% on hover | More restraint than Abyssal's framed cards. |
| Input | `#212121 / .65` blur tint, with form opacity `.6` and focus opacity `1` | Focus border uses the primary blue setting. |
| Shadow / glow | Canonical `#000000 / .5`; text-derived mixes for small glows | Many fine effects depend on runtime SillyTavern variables. |
| Status | `#e53935` error, `#9ccc65 / .8` success; progress error `#bd362f` | CSS-defined utility colors. |

Echo's user/character differentiation is chiefly **surface alpha and composition**, not a second accent palette. The portrait is an image masked into the message, while text padding reserves its space (`style.css:1406–1531`). The 26 gradients in `style.css` are mask gradients, not painted color ramps. The related config/preset gradient values also feed masks (`style.css:876–877,2473–2474`); their black stops are excluded from paint counts. Glimmer instead uses a near-neutral user surface `#1e1e1e / .30`, a pale character surface `#ffffff / .05`, and may replace the secondary gold with white. Moonlit's `color-mix()` supplies many border and hover alphas from body text and blue without introducing new RGB bases.

## 5. Cross-theme comparison

| Visual role | Abyssal | Honeyed | Moonlit Echoes | Reading for v1 |
| --- | --- | --- | --- | --- |
| App background | `#01040b`, `#030a15` | `#1a1410` | Transparent over wallpaper | Keep Abyssal navy and artwork. |
| Panel surface | `#061326 / .88`, `#08162a` | `#1a140f / .55–.65` | `#212121 / .65` | Borrow semantic glass roles, retain blue-black hue. |
| Message surface | Bubble `#040f1f / .96`; Minimal `#040f1f / .82` | Component fill unavailable | User `#2d2d2d / .50`; character `#272727 / .65` | Use one navy family with deliberate role/alpha difference. |
| Primary text | `#e7effb` | `#e8dcca` | `#cccccc` | Preserve Abyssal starlight. |
| Muted text | `#a8b8cd`, `#7f93ac` | `#9e8668` | `#969696` | Lower metadata emphasis without losing contrast. |
| Gold accent | `#e8cf91` plus name gradient | `#c4943a` primary | `#fac679` secondary | Keep Abyssal pale gold, use sparingly. |
| Blue accent | `#587eaf`, `#83afe0` | No equivalent | `#51a0de` | Keep Abyssal blue; refine focus/interactive contrast. |
| Border | `#5277a3 / .30`; Bubble `#6d91c3 / .14` | `#8f6e3d / .15` | Canonical transparent, input text-derived | Reduce message framing; keep subtle blue edges. |
| Input background | Navy glass family | `#1a140f / .55` | `#212121 / .65` before form opacity | Build an Abyssal navy glass input with clear focus. |

## 6. Usage and frequency findings

These are approximate **source-code literal** metrics, not computed-style frequencies. A token consumed internally by Lumiverse or a dynamic `color-mix()` can have much greater visual use than its literal count suggests. Moonlit figures combine the canonical preset, two Glimmer alternatives, and the extension settings UI.

| Theme | Literal occurrences | Unique source spellings | Unique normalized color + alpha | Unique RGB bases | Color + alpha values used once |
| --- | ---: | ---: | ---: | ---: | ---: |
| Abyssal | 193 | 159 | 153 | 76 | 125 |
| Honeyed | 27 | 23 | 23 | 20 | 20 |
| Moonlit Echoes | 54 | 33 | 30 | 19 | 17 |

| Theme | Most repeated literal families | Frequent named color-variable references | Alpha variants per notable base |
| --- | --- | --- | --- |
| Abyssal | White overlays 41; black shadows/overlays 28; `#6d91c3` family 10; `#030c1b` family 7 | `--lumiverse-bg` 3, `--muted` 3, `--ink` 2; many Lumiverse theme variables are consumed outside this CSS | White 26, black 16, `#6d91c3` 7, `#030c1b` 7, `#5277a3` 5 |
| Honeyed | Warm panel `#1a140f` 3; warm border `#8f6e3d / .15` 3; amber `#c4943a` 2 | `--ht-accent` 9; other named surface tokens usually referenced once | `#1a140f` 2, `#140f0b` 2; amber additionally has 9 `color-mix()` percentages |
| Moonlit Echoes | White overlays 13; black shadows 10; `#1e1e1e` and `#c6c6c6` families 4–5; blue `#51a0de` 4 | `--SmartThemeBodyColor` 103, `--customThemeColor` 79, `--SmartThemeBlurTintColor` 32, user tint 7, character tint 6 | White 5, black 4, `#1e1e1e` 3, `#c6c6c6` 3; many more dynamic mixes |

Approximately 125 Abyssal, 20 Honeyed, and 17 Moonlit normalized color/alpha values occur only once. These are **diagnostic counts**: gradients, a single focus state, or a specific shadow can justify a one-off. Abyssal's 76 RGB bases and two separately authored gold gradients are the clearest consolidation opportunities. Honeyed's low literal count follows from token and mix use. Moonlit's low literal count follows from preset/runtime variables and mask-based composition.

## 7. Design observations

1. The strongest shared roles are dark translucent surfaces, light primary text, quieter metadata, low-alpha edges, and black depth shadows. The hues differ substantially.
2. Abyssal blue-black and pale gold should anchor the rebuild. Honeyed's warm brown/amber is useful for token organization only. Moonlit's neutral charcoal is useful for opacity and contrast relationships only.
3. Bubble and Minimal currently choose related navy bases but independently tune alpha and borders. A shared message surface pair can express author differences without separate palette systems.
4. The visibly warm Abyssal names use many near-neighbor hex stops. One pale-gold base plus a short decorative ramp can carry that identity; routine borders and actions should stay blue.
5. Moonlit's Echo input and messages use few painted gradient colors. Portrait masking, translucency, opacity, and spacing create much of the effect. Do not import mask blacks as palette tokens.
6. The CSS/metadata primary mismatch, unused fallback values, and early purple/orange literals make direct token extraction from every old declaration unsafe. Select values from the final visual behavior and verify them in Lumiverse.

## 8. Proposed Abyssal v1 token palette

**Proposal only.** Values come from Abyssal's navy, text, blue, link, gold, and status families. Moonlit informs message alpha and contrast hierarchy; Honeyed informs role naming. RGB channels support deliberate alpha variants without new near-identical hex colors.

```css
:root {
  --ac-navy-rgb: 3 10 21;
  --ac-glass-rgb: 6 19 38;
  --ac-blue-rgb: 88 126 175;
  --ac-cyan-rgb: 131 175 224;
  --ac-gold-rgb: 232 207 145;

  --ac-bg-root: #01040b;
  --ac-bg-surface: #030a15;
  --ac-bg-surface-raised: #08162a;
  --ac-bg-glass: rgb(var(--ac-glass-rgb) / .78);
  --ac-bg-input: rgb(var(--ac-glass-rgb) / .68);
  --ac-message-character: rgb(4 15 31 / .82);
  --ac-message-user: rgb(8 22 42 / .74);

  --ac-text-primary: #e7effb;
  --ac-text-secondary: #a8b8cd;
  --ac-text-muted: #7f93ac;

  --ac-accent-gold: #e8cf91;
  --ac-accent-gold-soft: rgb(var(--ac-gold-rgb) / .16);
  --ac-accent-blue: #587eaf;
  --ac-accent-cyan: #83afe0;

  --ac-border-subtle: rgb(var(--ac-blue-rgb) / .22);
  --ac-border-strong: rgb(var(--ac-blue-rgb) / .44);
  --ac-hover: rgb(var(--ac-blue-rgb) / .16);
  --ac-focus: rgb(var(--ac-cyan-rgb) / .42);
  --ac-selection: rgb(var(--ac-cyan-rgb) / .30);
  --ac-shadow: rgb(0 0 0 / .28);
  --ac-glow-gold: rgb(var(--ac-gold-rgb) / .18);
  --ac-glow-blue: rgb(var(--ac-blue-rgb) / .20);

  --ac-status-danger: #c66b78;
  --ac-status-success: #559b96;
  --ac-status-warning: #c79b5d;
}
```

The `--ac-message-*` values are starting points for visual testing, not claims of current parity. The separate cyan role uses Abyssal's existing link blue; it should survive only if interaction states benefit from a lighter cool accent. A final implementation can expose fewer tokens if roles merge cleanly.

## 9. Open questions and visual verification

- Which primary wins in a fresh Lumiverse import: JSON `#0b72ff` or CSS `#587eaf`? Inspect computed styles and theme-manager output before finalizing the Lumiverse primary mapping.
- How should the two packaged artwork assets appear once their CSS URL/manifest mismatch is fixed? Compare a fresh import with the current visual reference.
- Honeyed's local bundle lacks its referenced BubbleMessage component CSS. Its actual message fill and border behavior remain unmapped.
- Moonlit values depend on SillyTavern's active preset, wallpaper, and runtime variables. Compare against the canonical preset when reviewing Echo screenshots; Glimmer is a distinct alternative.
- Confirm legibility and contrast of proposed `.74–.82` message glass, subdued metadata, and focus blue over the actual constellation and moon backgrounds on desktop and mobile.
- Confirm whether Abyssal needs a separate cyan token after visual testing; current evidence is a lighter blue link color rather than a distinct cyan family.

## Appendix — Literal color inventory

The tables below list each included source spelling once. Uses count all included appearances in the inspected sources; the role and source identify the **first** appearance and may not describe every use of that spelling. JSON `globalCSS` line numbers are decoded CSS lines. Mask-only colors, transparent stops, inactive fallbacks, and dynamically computed colors follow the exclusions in Methodology.

### Abyssal Constellation literal inventory

| Original syntax | Normalized base / alpha | Uses | Approximate role | First source | Variable / key |
| --- | --- | ---: | --- | --- | --- |
| `rgba(255, 255, 255, 0.035)` | `#ffffff / 0.035` | 4 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):183` | — |
| `rgba(255, 255, 255, 0.08)` | `#ffffff / 0.08` | 4 | border | `reference/Abyssal Constellation/theme.json (globalCSS):167` | `--line` |
| `#6d91c3` | `#6d91c3` | 3 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):5` | `--lumiverse-primary-hover` |
| `rgba(255, 255, 255, 0.018)` | `#ffffff / 0.018` | 3 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1433` | — |
| `rgba(255, 255, 255, 0.045)` | `#ffffff / 0.045` | 3 | border | `reference/Abyssal Constellation/theme.json (globalCSS):434` | — |
| `#01040b` | `#01040b` | 2 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):15` | `--lumiverse-bg-deep` |
| `#030a15` | `#030a15` | 2 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):10` | `--lumiverse-bg` |
| `#559b96` | `#559b96` | 2 | status | `reference/Abyssal Constellation/theme.json:22` | `theme.statusColors.success` |
| `#91b5df` | `#91b5df` | 2 | text | `reference/Abyssal Constellation/theme.json (globalCSS):50` | `--lumiverse-prose-dialogue` |
| `#9fb0c6` | `#9fb0c6` | 2 | text | `reference/Abyssal Constellation/theme.json (globalCSS):48` | `--lumiverse-prose-italic` |
| `#c66b78` | `#c66b78` | 2 | status | `reference/Abyssal Constellation/theme.json:21` | `theme.statusColors.danger` |
| `#c79b5d` | `#c79b5d` | 2 | status | `reference/Abyssal Constellation/theme.json:23` | `theme.statusColors.warning` |
| `#e7effb` | `#e7effb` | 2 | text | `reference/Abyssal Constellation/theme.json (globalCSS):17` | `--lumiverse-text` |
| `#f3dfa7` | `#f3dfa7` | 2 | text | `reference/Abyssal Constellation/theme.json (globalCSS):1758` | — |
| `#f6dfa1` | `#f6dfa1` | 2 | text | `reference/Abyssal Constellation/theme.json (globalCSS):921` | — |
| `rgb(0 0 0 / 16%)` | `#000000 / 0.16` | 2 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1550` | `--me-content-glass-shadow` |
| `rgb(0 0 0 / 22%)` | `#000000 / 0.22` | 2 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):769` | — |
| `rgb(109 145 195 / 14%)` | `#6d91c3 / 0.14` | 2 | border | `reference/Abyssal Constellation/theme.json (globalCSS):750` | `--line` |
| `rgba(0, 0, 0, 0.12)` | `#000000 / 0.12` | 2 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):217` | — |
| `rgba(0, 0, 0, 0.18)` | `#000000 / 0.18` | 2 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):323` | — |
| `rgba(0, 0, 0, 0.2)` | `#000000 / 0.2` | 2 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):652` | — |
| `rgba(0, 0, 0, 0.86)` | `#000000 / 0.86` | 2 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):651` | — |
| `rgba(0, 0, 0, 0.95)` | `#000000 / 0.95` | 2 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):322` | — |
| `rgba(255, 255, 255, 0.055)` | `#ffffff / 0.055` | 2 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):462` | — |
| `rgba(255, 255, 255, 0.065)` | `#ffffff / 0.065` | 2 | border | `reference/Abyssal Constellation/theme.json (globalCSS):1425` | — |
| `rgba(255, 255, 255, 0.075)` | `#ffffff / 0.075` | 2 | border | `reference/Abyssal Constellation/theme.json (globalCSS):421` | — |
| `rgba(255, 255, 255, 0.12)` | `#ffffff / 0.12` | 2 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):557` | — |
| `#01050d` | `#01050d` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):14` | `--lumiverse-bg-darker` |
| `#020711` | `#020711` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):13` | `--lumiverse-bg-dark` |
| `#08162a` | `#08162a` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):11` | `--lumiverse-bg-elevated` |
| `#0b72ff` | `#0b72ff` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json:27` | `theme.baseColorsByMode.dark.primary` |
| `#0c1d34` | `#0c1d34` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):12` | `--lumiverse-bg-hover` |
| `#36577f` | `#36577f` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):7` | `--lumiverse-primary-muted` |
| `#587eaf` | `#587eaf` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):4` | `--lumiverse-primary` |
| `#61758f` | `#61758f` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):20` | `--lumiverse-text-hint` |
| `#7f93ac` | `#7f93ac` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):19` | `--lumiverse-text-dim` |
| `#82a5d1` | `#82a5d1` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):25` | `--lumiverse-secondary-hover` |
| `#83afe0` | `#83afe0` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):52` | `--lumiverse-prose-link` |
| `#8499b2` | `#8499b2` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):27` | `--lumiverse-icon-muted` |
| `#8ba9cf` | `#8ba9cf` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):6` | `--lumiverse-primary-light` |
| `#8ca8c9` | `#8ca8c9` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):51` | `--lumiverse-prose-blockquote` |
| `#a8b8cd` | `#a8b8cd` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):18` | `--lumiverse-text-muted` |
| `#b7c9df` | `#b7c9df` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):26` | `--lumiverse-icon` |
| `#b98f47` | `#b98f47` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):897` | — |
| `#b99149` | `#b99149` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1736` | — |
| `#b9d0eb` | `#b9d0eb` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):8` | `--lumiverse-primary-text` |
| `#c9a45d` | `#c9a45d` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):893` | — |
| `#cda95e` | `#cda95e` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1732` | — |
| `#d5b66e` | `#d5b66e` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1735` | — |
| `#dfc278` | `#dfc278` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):896` | — |
| `#e8cf91` | `#e8cf91` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):1726` | — |
| `#efd79a` | `#efd79a` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):894` | — |
| `#efd99c` | `#efd99c` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):889` | — |
| `#f1f6fd` | `#f1f6fd` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):49` | `--lumiverse-prose-bold` |
| `#f2dfaa` | `#f2dfaa` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1733` | — |
| `#fff1c8` | `#fff1c8` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1734` | — |
| `#fff2ca` | `#fff2ca` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):895` | — |
| `rgb(0 0 0 / 12%)` | `#000000 / 0.12` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1817` | — |
| `rgb(0 0 0 / 54%)` | `#000000 / 0.54` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):908` | — |
| `rgb(0 3 9 / 76%)` | `#000309 / 0.76` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):46` | `--lumiverse-modal-backdrop` |
| `rgb(1 4 11 / 12%)` | `#01040b / 0.12` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):109` | — |
| `rgb(1 4 11 / 22%)` | `#01040b / 0.22` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):60` | — |
| `rgb(1 4 11 / 8%)` | `#01040b / 0.08` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):60` | — |
| `rgb(10 28 52 / 84%)` | `#0a1c34 / 0.84` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):29` | `--lumiverse-fill` |
| `rgb(10 30 56 / 58%)` | `#0a1e38 / 0.58` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1810` | — |
| `rgb(109 145 195 / 13%)` | `#6d91c3 / 0.13` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):1548` | `--me-content-glass-border` |
| `rgb(109 145 195 / 18%)` | `#6d91c3 / 0.18` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):752` | `--accent-warm` |
| `rgb(109 145 195 / 20%)` | `#6d91c3 / 0.2` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):1814` | — |
| `rgb(109 145 195 / 44%)` | `#6d91c3 / 0.44` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):40` | `--lcs-glass-border-hover` |
| `rgb(109 145 195 / 48%)` | `#6d91c3 / 0.48` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):23` | `--lumiverse-border-hover` |
| `rgb(11 31 57 / 92%)` | `#0b1f39 / 0.92` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):38` | `--lcs-glass-bg-hover` |
| `rgb(117 157 210 / 15%)` | `#759dd2 / 0.15` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1762` | — |
| `rgb(12 35 64 / 70%)` | `#0c2340 / 0.7` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1834` | — |
| `rgb(13 37 68 / 52%)` | `#0d2544 / 0.52` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):757` | — |
| `rgb(133 171 221 / 8%)` | `#85abdd / 0.08` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1744` | — |
| `rgb(145 181 223 / 34%)` | `#91b5df / 0.34` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):1838` | — |
| `rgb(168 184 205 / 58%)` | `#a8b8cd / 0.58` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):1825` | — |
| `rgb(168 184 205 / 72%)` | `#a8b8cd / 0.72` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):749` | `--muted` |
| `rgb(18 43 75 / 88%)` | `#122b4b / 0.88` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):31` | `--lumiverse-fill-hover` |
| `rgb(19 45 78 / 88%)` | `#132d4e / 0.88` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):81` | — |
| `rgb(2 10 23 / 86%)` | `#020a17 / 0.86` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):953` | — |
| `rgb(2 10 23 / 98%)` | `#020a17 / 0.98` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):764` | — |
| `rgb(2 8 18 / 99%)` | `#020812 / 0.99` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):35` | `--lumiverse-fill-deepest` |
| `rgb(226 195 116 / 13%)` | `#e2c374 / 0.13` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1743` | — |
| `rgb(231 239 251 / 94%)` | `#e7effb / 0.94` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):748` | `--ink` |
| `rgb(244 213 137 / 16%)` | `#f4d589 / 0.16` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):907` | — |
| `rgb(244 213 137 / 40%)` | `#f4d589 / 0.4` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):906` | — |
| `rgb(245 218 148 / 38%)` | `#f5da94 / 0.38` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1761` | — |
| `rgb(247 222 160 / 22%)` | `#f7dea0 / 0.22` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):925` | — |
| `rgb(247 222 160 / 54%)` | `#f7dea0 / 0.54` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):924` | — |
| `rgb(255 255 255 / 2%)` | `#ffffff / 0.02` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):770` | — |
| `rgb(255 255 255 / 2.5%)` | `#ffffff / 0.025` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1816` | — |
| `rgb(3 10 21 / 38%)` | `#030a15 / 0.38` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):110` | — |
| `rgb(3 10 21 / 96%)` | `#030a15 / 0.96` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):111` | — |
| `rgb(3 12 27 / 18%)` | `#030c1b / 0.18` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1856` | — |
| `rgb(3 12 27 / 26%)` | `#030c1b / 0.26` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1855` | — |
| `rgb(3 12 27 / 64%)` | `#030c1b / 0.64` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1667` | — |
| `rgb(3 12 27 / 76%)` | `#030c1b / 0.76` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1666` | — |
| `rgb(3 12 27 / 8%)` | `#030c1b / 0.08` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1857` | — |
| `rgb(3 12 27 / 88%)` | `#030c1b / 0.88` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1558` | — |
| `rgb(3 12 27 / 99%)` | `#030c1b / 0.99` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):73` | — |
| `rgb(4 15 31 / 72%)` | `#040f1f / 0.72` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):1547` | `--me-content-glass-bg` |
| `rgb(4 15 31 / 82%)` | `#040f1f / 0.82` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1665` | — |
| `rgb(4 15 31 / 96%)` | `#040f1f / 0.96` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):763` | — |
| `rgb(4 16 34 / 48%)` | `#041022 / 0.48` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1811` | — |
| `rgb(4 16 34 / 88%)` | `#041022 / 0.88` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):87` | — |
| `rgb(5 17 34 / 97%)` | `#051122 / 0.97` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):34` | `--lumiverse-fill-heavy` |
| `rgb(5 18 37 / 76%)` | `#051225 / 0.76` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):952` | — |
| `rgb(5 19 39 / 62%)` | `#051327 / 0.62` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1835` | — |
| `rgb(6 19 38 / 88%)` | `#061326 / 0.88` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):37` | `--lcs-glass-bg` |
| `rgb(6 20 40 / 28%)` | `#061428 / 0.28` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):758` | — |
| `rgb(7 21 41 / 90%)` | `#071529 / 0.9` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):45` | `--lumiverse-card-bg` |
| `rgb(7 22 43 / 95%)` | `#07162b / 0.95` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):33` | `--lumiverse-fill-strong` |
| `rgb(8 22 42 / 62%)` | `#08162a / 0.62` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):30` | `--lumiverse-fill-subtle` |
| `rgb(8 25 48 / 72%)` | `#081930 / 0.72` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1557` | — |
| `rgb(82 119 163 / 18%)` | `#5277a3 / 0.18` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):1560` | — |
| `rgb(82 119 163 / 26%)` | `#5277a3 / 0.26` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):39` | `--lcs-glass-border` |
| `rgb(82 119 163 / 28%)` | `#5277a3 / 0.28` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):88` | — |
| `rgb(82 119 163 / 30%)` | `#5277a3 / 0.3` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):22` | `--lumiverse-border` |
| `rgb(82 119 163 / 32%)` | `#5277a3 / 0.32` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):74` | — |
| `rgb(88 126 175 / 12%)` | `#587eaf / 0.12` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1840` | — |
| `rgb(88 126 175 / 16%)` | `#587eaf / 0.16` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1869` | — |
| `rgb(88 126 175 / 26%)` | `#587eaf / 0.26` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):751` | `--accent-soft` |
| `rgb(9 26 50 / 91%)` | `#091a32 / 0.91` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):32` | `--lumiverse-fill-medium` |
| `rgb(9 27 52 / 98%)` | `#091b34 / 0.98` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):73` | — |
| `rgba(0, 0, 0, 0.04)` | `#000000 / 0.04` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):216` | — |
| `rgba(0, 0, 0, 0.16)` | `#000000 / 0.16` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1434` | — |
| `rgba(0, 0, 0, 0.20)` | `#000000 / 0.2` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1465` | — |
| `rgba(0, 0, 0, 0.22)` | `#000000 / 0.22` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):394` | — |
| `rgba(0, 0, 0, 0.28)` | `#000000 / 0.28` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):461` | — |
| `rgba(0, 0, 0, 0.34)` | `#000000 / 0.34` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):516` | — |
| `rgba(0, 0, 0, 0.38)` | `#000000 / 0.38` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):182` | — |
| `rgba(0, 0, 0, 0.42)` | `#000000 / 0.42` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):555` | — |
| `rgba(0, 0, 0, 0.65)` | `#000000 / 0.65` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):406` | — |
| `rgba(0,0,0,0.08)` | `#000000 / 0.08` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1480` | — |
| `rgba(0,0,0,0.14)` | `#000000 / 0.14` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1479` | — |
| `rgba(0,0,0,0.2)` | `#000000 / 0.2` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1478` | — |
| `rgba(18, 16, 28, 0.55)` | `#12101c / 0.55` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1475` | — |
| `rgba(181, 139, 255, 0.08)` | `#b58bff / 0.08` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):556` | — |
| `rgba(181, 139, 255, 0.22)` | `#b58bff / 0.22` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):312` | — |
| `rgba(181, 139, 255, 0.3)` | `#b58bff / 0.3` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):168` | `--accent-soft` |
| `rgba(255, 129, 84, 0.25)` | `#ff8154 / 0.25` | 1 | accent/interaction | `reference/Abyssal Constellation/theme.json (globalCSS):169` | `--accent-warm` |
| `rgba(255, 255, 255, 0.012)` | `#ffffff / 0.012` | 1 | shadow/glow | `reference/Abyssal Constellation/theme.json (globalCSS):1364` | — |
| `rgba(255, 255, 255, 0.015)` | `#ffffff / 0.015` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):540` | — |
| `rgba(255, 255, 255, 0.025)` | `#ffffff / 0.025` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):512` | — |
| `rgba(255, 255, 255, 0.085)` | `#ffffff / 0.085` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):390` | — |
| `rgba(255, 255, 255, 0.09)` | `#ffffff / 0.09` | 1 | surface/overlay | `reference/Abyssal Constellation/theme.json (globalCSS):563` | — |
| `rgba(255, 255, 255, 0.1)` | `#ffffff / 0.1` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):514` | — |
| `rgba(255, 255, 255, 0.11)` | `#ffffff / 0.11` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):458` | — |
| `rgba(255, 255, 255, 0.16)` | `#ffffff / 0.16` | 1 | border | `reference/Abyssal Constellation/theme.json (globalCSS):553` | — |
| `rgba(255, 255, 255, 0.58)` | `#ffffff / 0.58` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):539` | — |
| `rgba(255, 255, 255, 0.62)` | `#ffffff / 0.62` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):166` | `--muted` |
| `rgba(255, 255, 255, 0.68)` | `#ffffff / 0.68` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):310` | — |
| `rgba(255, 255, 255, 0.86)` | `#ffffff / 0.86` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):438` | — |
| `rgba(255, 255, 255, 0.9)` | `#ffffff / 0.9` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):562` | — |
| `rgba(255, 255, 255, 0.92)` | `#ffffff / 0.92` | 1 | text | `reference/Abyssal Constellation/theme.json (globalCSS):165` | `--ink` |
| `rgba(255,255,255,0.007)` | `#ffffff / 0.007` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1474` | — |
| `rgba(255,255,255,0.013)` | `#ffffff / 0.013` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1474` | — |
| `rgba(255,255,255,0.022)` | `#ffffff / 0.022` | 1 | gradient stop | `reference/Abyssal Constellation/theme.json (globalCSS):1474` | — |

### Honeyed Twilight literal inventory

| Original syntax | Normalized base / alpha | Uses | Approximate role | First source | Variable / key |
| --- | --- | ---: | --- | --- | --- |
| `hsla(36, 40%, 40%, 0.15)` | `#8f6e3d / 0.15` | 3 | border | `reference/Honeyed Twilight/theme.json (globalCSS):91` | `--ht-modal-border` |
| `#c4943a` | `#c4943a` | 2 | accent/interaction | `reference/Honeyed Twilight/theme.json (globalCSS):64` | `--ht-accent-fallback` |
| `hsla(26, 28%, 8%, 0.55)` | `#1a140f / 0.55` | 2 | surface/overlay | `reference/Honeyed Twilight/theme.json (globalCSS):76` | `--ht-glass-tint` |
| `#1a1410` | `#1a1410` | 1 | surface/overlay | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.background` |
| `#4aad5c` | `#4aad5c` | 1 | status | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.success` |
| `#6b5a42` | `#6b5a42` | 1 | accent/interaction | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.secondary` |
| `#9e8668` | `#9e8668` | 1 | text | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.thoughts` |
| `#d4992e` | `#d4992e` | 1 | status | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.warning` |
| `#d4a246` | `#d4a246` | 1 | text | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.speech` |
| `#d94848` | `#d94848` | 1 | status | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.danger` |
| `#e8dcca` | `#e8dcca` | 1 | text | `reference/Honeyed Twilight/theme.json:1` | `theme.baseColorsByMode.dark.text` |
| `hsla(26, 28%, 10%, 0.60)` | `#211912 / 0.6` | 1 | accent/interaction | `reference/Honeyed Twilight/theme.json (globalCSS):77` | `--ht-glass-tint-hover` |
| `hsla(26, 28%, 15%, 0.50)` | `#31251c / 0.5` | 1 | accent/interaction | `reference/Honeyed Twilight/theme.json (globalCSS):83` | `--ht-settings-nav-hover` |
| `hsla(26, 28%, 18%, 0.60)` | `#3b2c21 / 0.6` | 1 | accent/interaction | `reference/Honeyed Twilight/theme.json (globalCSS):84` | `--ht-settings-nav-active` |
| `hsla(26, 28%, 4%, 0.30)` | `#0d0a07 / 0.3` | 1 | surface/overlay | `reference/Honeyed Twilight/theme.json (globalCSS):90` | `--ht-modal-backdrop` |
| `hsla(26, 28%, 6%, 0.52)` | `#140f0b / 0.52` | 1 | surface/overlay | `reference/Honeyed Twilight/theme.json (globalCSS):72` | `--ht-drawer-toggle-button` |
| `hsla(26, 28%, 6%, 0.70)` | `#140f0b / 0.7` | 1 | text | `reference/Honeyed Twilight/theme.json (globalCSS):71` | `--ht-drawer-icon-strip` |
| `hsla(26, 28%, 8%, 0.65)` | `#1a140f / 0.65` | 1 | surface/overlay | `reference/Honeyed Twilight/theme.json (globalCSS):70` | `--ht-drawer-panel` |
| `hsla(30, 30%, 15%, 0.25)` | `#32261b / 0.25` | 1 | accent/interaction | `reference/Honeyed Twilight/theme.json (globalCSS):82` | `--ht-tab-hover` |
| `hsla(30, 35%, 10%, 0.85)` | `#221a11 / 0.85` | 1 | surface/overlay | `reference/Honeyed Twilight/theme.json (globalCSS):89` | `--ht-modal` |
| `hsla(30, 35%, 15%, 0.35)` | `#342619 / 0.35` | 1 | accent/interaction | `reference/Honeyed Twilight/theme.json (globalCSS):81` | `--ht-tab-active` |
| `rgba(0, 0, 0, 0.12)` | `#000000 / 0.12` | 1 | shadow/glow | `reference/Honeyed Twilight/theme.json (globalCSS):103` | `--ht-message-shadow-soft` |
| `rgba(0, 0, 0, 0.20)` | `#000000 / 0.2` | 1 | shadow/glow | `reference/Honeyed Twilight/theme.json (globalCSS):104` | `--ht-message-shadow-medium` |

### Moonlit Echoes literal inventory

| Original syntax | Normalized base / alpha | Uses | Approximate role | First source | Variable / key |
| --- | --- | ---: | --- | --- | --- |
| `rgba(0, 0, 0, 0.3)` | `#000000 / 0.3` | 6 | shadow/glow | `reference/Moonlit Echoes/style.css:3489` | — |
| `rgba(81, 160, 222, 1)` | `#51a0de` | 4 | accent/interaction | `reference/Moonlit Echoes/src/config/theme-settings.js:42` | `--customThemeColor` |
| `rgba(255, 255, 255, 0.05)` | `#ffffff / 0.05` | 3 | surface/overlay | `reference/Moonlit Echoes/src/config/theme-settings.js:66` | `--customBgColor2` |
| `rgba(255, 255, 255, 0.5)` | `#ffffff / 0.5` | 3 | text | `reference/Moonlit Echoes/style.css:649` | — |
| `rgba(30, 30, 30, 1)` | `#1e1e1e` | 3 | surface/overlay | `reference/Moonlit Echoes/theme/[Moonlit] Glimmer - by Rivelle.json:10` | `settings.customTopBarColor` |
| `#FFF` | `#ffffff` | 2 | text | `reference/Moonlit Echoes/style.css:132` | — |
| `rgb(229, 57, 53)` | `#e53935` | 2 | status | `reference/Moonlit Echoes/style.css:36` | `--fullred` |
| `rgba(170, 170, 170, 0.15)` | `#aaaaaa / 0.15` | 2 | text | `reference/Moonlit Echoes/style.css:3177` | — |
| `rgba(198, 198, 198, 1)` | `#c6c6c6` | 2 | text | `reference/Moonlit Echoes/theme/[Moonlit] Glimmer - by Rivelle.json:11` | `settings.Drawer-iconColor` |
| `rgba(225, 225, 225, 0.2)` | `#e1e1e1 / 0.2` | 2 | surface/overlay | `reference/Moonlit Echoes/style.css:1544` | — |
| `rgba(250, 198, 121, 1)` | `#fac679` | 2 | accent/interaction | `reference/Moonlit Echoes/src/config/theme-settings.js:50` | `--customThemeColor2` |
| `rgba(255, 255, 255, 0.1)` | `#ffffff / 0.1` | 2 | surface/overlay | `reference/Moonlit Echoes/src/config/theme-settings.js:58` | `--customBgColor1` |
| `#fff` | `#ffffff` | 1 | text | `reference/Moonlit Echoes/style.css:581` | — |
| `rgb(156, 204, 101, 0.8)` | `#9ccc65 / 0.8` | 1 | status | `reference/Moonlit Echoes/style.css:42` | `--okGreen70a` |
| `rgb(189, 54, 47)` | `#bd362f` | 1 | status | `reference/Moonlit Echoes/style.css:2363` | `--progErrorColor` |
| `rgba(0, 0, 0, 0.2)` | `#000000 / 0.2` | 1 | surface/overlay | `reference/Moonlit Echoes/src/config/theme-settings.js:90` | `--sheldBackgroundColor` |
| `rgba(0, 0, 0, 0.5)` | `#000000 / 0.5` | 1 | shadow/glow | `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:12` | `shadow_color` |
| `rgba(0, 0, 0, 3%)` | `#000000 / 0.03` | 1 | shadow/glow | `reference/Moonlit Echoes/style.css:1396` | — |
| `rgba(0,0,0,3%)` | `#000000 / 0.03` | 1 | shadow/glow | `reference/Moonlit Echoes/style.css:1001` | — |
| `rgba(108, 108, 108, 1)` | `#6c6c6c` | 1 | text | `reference/Moonlit Echoes/theme/Glimmer - by Rivelle.json:5` | `italics_text_color` |
| `rgba(150, 150, 150, 1)` | `#969696` | 1 | text | `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:5` | `italics_text_color` |
| `rgba(198, 198, 198, 0.1)` | `#c6c6c6 / 0.1` | 1 | border | `reference/Moonlit Echoes/theme/Glimmer - by Rivelle.json:14` | `border_color` |
| `rgba(198, 198, 198, 0.5)` | `#c6c6c6 / 0.5` | 1 | surface/overlay | `reference/Moonlit Echoes/theme/[Moonlit] Glimmer - by Rivelle.json:13` | `settings.customScrollbarColor` |
| `rgba(204, 204, 204, 1)` | `#cccccc` | 1 | text | `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:4` | `main_text_color` |
| `rgba(223, 223, 223, 1)` | `#dfdfdf` | 1 | text | `reference/Moonlit Echoes/theme/Glimmer - by Rivelle.json:6` | `underline_text_color` |
| `rgba(23, 23, 23, 0.7)` | `#171717 / 0.7` | 1 | surface/overlay | `reference/Moonlit Echoes/src/config/theme-settings.js:74` | `--customTopBarColor` |
| `rgba(255, 255, 255, 0.8)` | `#ffffff / 0.8` | 1 | text | `reference/Moonlit Echoes/src/config/theme-settings.js:82` | `--Drawer-iconColor` |
| `rgba(255, 255, 255, 1)` | `#ffffff` | 1 | accent/interaction | `reference/Moonlit Echoes/theme/[Moonlit] Glimmer - by Rivelle.json:7` | `settings.customThemeColor2` |
| `rgba(30, 30, 30, 0.3)` | `#1e1e1e / 0.3` | 1 | surface/overlay | `reference/Moonlit Echoes/theme/Glimmer - by Rivelle.json:10` | `user_mes_blur_tint_color` |
| `rgba(30, 30, 30, 0.6)` | `#1e1e1e / 0.6` | 1 | surface/overlay | `reference/Moonlit Echoes/theme/[Moonlit] Glimmer - by Rivelle.json:12` | `settings.sheldBackgroundColor` |
| `rgba(33, 33, 33, 0.65)` | `#212121 / 0.65` | 1 | surface/overlay | `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:8` | `blur_tint_color` |
| `rgba(39, 39, 39, 0.65)` | `#272727 / 0.65` | 1 | surface/overlay | `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:11` | `bot_mes_blur_tint_color` |
| `rgba(45, 45, 45, 0.5)` | `#2d2d2d / 0.5` | 1 | surface/overlay | `reference/Moonlit Echoes/theme/Moonlit Echoes - by Rivelle.json:10` | `user_mes_blur_tint_color` |

