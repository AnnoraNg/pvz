# Prompt for Codex — round 2 (title screen + UI art) — copy everything below this line

---

The game `pvz.html` in this folder loads art from `assets/` by exact filename. The sprites (plants/zombies/projectiles) and the main `background.png` are done — **do not touch any existing file in `assets/`**. This round: generate the title screen and UI art. Save every file into `assets/` with the exact filename and exact pixel dimensions below. Wrong name or size = the game silently ignores it.

## Global style

- Target quality: polished commercial 2D game (think hand-painted PopCap/Rayman-style production art), NOT flat programmer-art or clip-art. Rich color grading, soft painted texture, subtle gradients, ambient occlusion where objects meet the ground, warm afternoon key light from the top-left.
- Original artwork inspired by the lawn-defense genre; do not copy actual Plants vs. Zombies assets.
- All files PNG. Files marked *transparent* must be PNG-24 RGBA with transparent background outside the artwork. No watermarks. No text anywhere except the logo (section 3).
- Exact pixel dimensions are mandatory — resize/crop before saving if needed.

## 1. Title screen background — `assets/menu_background.png` — 1000×660 (opaque)

The game's front yard at dusk (match the painterly style of the existing `assets/background.png` — look at it for reference), moody-but-fun: purple-orange sky, low full moon, light ground fog rolling over the lawn, a few crooked tombstones and silhouetted zombie hands/heads rising at the far right, warm porch light on the house at left. Composition requirements:
- Top area (y 10–290, centered) stays relatively clean sky — the logo overlays there.
- Center-bottom band (x 280–720, y 290–620) must be LOW-CONTRAST and dark-ish — five menu buttons overlay there and must stay readable.
- No text anywhere.

## 2. Logo — `assets/logo.png` — 640×280 (transparent)

Stylized game logo lettering, two stacked lines: "PLANTS" in big chunky letters made of grass/leaves with a small sunflower dotting a letter, "ZOMBIES" below it in cracked purple-grey tombstone letters with a bite taken out of one letter; a small hand-written "vs." connecting them. Slight arc/perspective, thick dark outline, drop shadow baked in is OK. Fill the canvas, transparent background. Spelling must be exactly: PLANTS vs. ZOMBIES.

## 3. HUD & UI elements

| Filename | Size | Transparent | Description |
|---|---|---|---|
| `assets/hud_bar.png` | 980×100 | yes (corners) | Horizontal HUD tray: polished dark wooden plank with carved border, brass corner rivets, subtle top highlight. Rounded corners (~10px radius, transparent outside). Center must stay plain — seed packets are drawn on top. |
| `assets/sun_counter.png` | 110×86 | yes (corners) | Small parchment/cream panel with thin wooden frame, rounded corners. Empty center — the game draws a sun icon in the upper half and the sun number in the lower half, so keep the middle plain and light. |
| `assets/seed_packet.png` | 68×86 | yes | Empty seed packet: brown-paper packet with a slightly torn top flap strip, thin inner frame, plain light lower third (a cost number is drawn there). NO plant inside — the game draws the plant art in the middle. |
| `assets/progress_frame.png` | 300×36 | yes | Level-progress bar frame: weathered wood/stone frame with a decorative small zombie head cap on the RIGHT end and a tiny flag on the LEFT end. The inner window must be transparent and exactly 280×16, centered (10px margin on every side) — the fill bar shows through it. |
| `assets/progress_fill.png` | 280×16 | no (opaque) | The fill bar itself: juicy green gel/liquid gradient with a bright top highlight, slightly darker right edge. Simple horizontal texture (it gets cropped from the left as progress grows). |
| `assets/button.png` | 220×60 | yes (corners) | Blank wooden button: horizontal plank with carved bevel edge, warm honey wood grain, subtle top-left highlight, rounded corners. NO text — labels are drawn on top. |
| `assets/button_wide.png` | 460×56 | yes (corners) | Same design language as `button.png` but wide — used for the level-select list. NO text. |
| `assets/banner_ribbon.png` | 720×100 | yes | Weathered red fabric ribbon/banner with darker folded ends and stitched border, gently curved, blank center (big announcement text is drawn on top). Slightly torn edges for drama. |

## 4. After generating — verify

```python
from PIL import Image
import os
spec = {  # filename: (w, h, must_be_rgba)
 'menu_background.png':(1000,660,False),
 'logo.png':(640,280,True), 'hud_bar.png':(980,100,True), 'sun_counter.png':(110,86,True),
 'seed_packet.png':(68,86,True), 'progress_frame.png':(300,36,True),
 'progress_fill.png':(280,16,False), 'button.png':(220,60,True),
 'button_wide.png':(460,56,True), 'banner_ribbon.png':(720,100,True),
}
for f,(w,h,rgba) in spec.items():
    p = os.path.join('assets', f)
    if not os.path.exists(p): print('MISSING', f); continue
    im = Image.open(p)
    ok = im.size==(w,h) and (not rgba or im.mode=='RGBA')
    print('OK  ' if ok else f'BAD {im.size} {im.mode}', f)
# progress_frame: inner 280x16 window must be transparent
fr = Image.open('assets/progress_frame.png').convert('RGBA')
alphas = [fr.getpixel((10+x, 18))[3] for x in range(0,280,20)]
print('frame window transparent:', 'OK' if max(alphas)<60 else f'FAIL {alphas}')
```

10 files total this round. Do not modify `pvz.html` or any existing file in `assets/` (plants, zombies, sun, peas, mower, shovel, background.png).
