# Prompt for Codex — round 4 (night world, fog world, full UI icon set) — copy everything below this line

---

The game `pvz.html` loads art from `assets/` by exact filename. Night and fog worlds plus new UI were added and need art. **Match the established art style exactly** (open existing files in `assets/` for reference — same painterly cartoon style, outlines, palette). PNG format, exact filenames and pixel dimensions below. Files marked *transparent* must be RGBA with transparent backgrounds. No text or watermarks anywhere. Do not modify existing files.

**IMPORTANT — fill the canvas:** in a previous round, several UI images had the artwork occupying only the middle third of the canvas with large transparent margins, which broke the game layout. The artwork must fill ~95% of each canvas, edge to edge, with at most 2–3px of transparent padding.

## 1. Night background — `assets/background_night.png` — 1000×660 (opaque)

The SAME front yard as `assets/background.png` (use it as the direct reference — same house, fence, layout) but at night: deep blue-purple sky with stars, a large glowing full moon in the upper right, cool moonlight grading, warm light spilling from the house window on the left. The lawn checkerboard must use exactly the same grid geometry as the day version: 9 columns × 92px, 5 rows × 98px spanning x 130→958, y 140→630, cell (c,r) lighter when (r+c) is even — but in darker, cooler night greens. The two tones must remain clearly distinguishable.

## 2. Night & fog gameplay sprites

Plants: 90×100, transparent, facing right, same framing as existing plants.

| Filename | Description |
|---|---|
| `assets/grave.png` | A weathered grey TOMBSTONE with cracks, moss, and tufts of grass at its base. Slightly crooked, ominous. (This is an obstacle, not a plant.) |
| `assets/sunshroom.png` | A small sleepy-cute mushroom with a softly GLOWING warm yellow cap, short stalk, gentle smile. Small — fills only ~60% of canvas height. |
| `assets/sunshroom_big.png` | The same mushroom fully grown: much bigger cap, brighter glow, prouder expression. Fills the canvas. |
| `assets/puffshroom.png` | A tiny timid purple puffball mushroom with big shy eyes, very small (~50% of canvas height), sitting low. |
| `assets/fumeshroom.png` | A stout purple mushroom with a wide green-tipped snout/spout aimed RIGHT, mid-exhale of a faint green fume wisp. |
| `assets/hypnoshroom.png` | A mesmerizing mushroom with a red-and-pink SWIRL pattern on its cap, dreamy half-closed spiral eyes. |
| `assets/plantern.png` | A plant-lantern: green stem holding up a glowing paper-lantern bulb radiating warm light, moth-friendly. |

Projectiles, transparent:

| Filename | Size | Description |
|---|---|---|
| `assets/puff.png` | 24×24 | A small soft purple spore puff with a wispy trail. |
| `assets/fume.png` | 64×32 | A translucent green fume cloud, denser on the left, dissipating to the right. |

Zombies: 110×140, transparent, facing LEFT, feet at bottom edge, same base zombie as existing:

| Filename | Description |
|---|---|
| `assets/zombie_screendoor.png` | Zombie carrying a full-size mesh SCREEN DOOR in front of him like a shield, peeking around it. |
| `assets/zombie_dancer.png` | Disco zombie: purple sequined suit, afro, one arm pointing up in a dance pose, gold medallion. |
| `assets/zombie_backup.png` | Smaller backup-dancer zombie: red outfit, mid dance-step pose, matching sunglasses. |

## 3. UI icon set (fill the canvas — minimal transparent padding!)

| Filename | Size | Description |
|---|---|---|
| `assets/minibtn.png` | 40×40 | Small square wooden button, carved bevel edge, rounded corners (~7px), matching `button.png` styling. Blank center. |
| `assets/minibtn_active.png` | 40×40 | Same button but golden/highlighted (pressed/active state). |
| `assets/icon_pause.png` | 24×24 | Two vertical pause bars, warm cream/gold color with dark outline. |
| `assets/icon_play.png` | 24×24 | Play triangle, same style. |
| `assets/icon_sound_on.png` | 24×24 | Speaker with sound waves, same style. |
| `assets/icon_sound_off.png` | 24×24 | Speaker with a red slash, same style. |
| `assets/lock.png` | 24×30 | A small brass padlock, closed. |
| `assets/card.png` | 100×124 | Blank parchment/wood seed-selection card frame: thin wooden border, plain light center (plant art + name + cost are drawn on top). Rounded corners ~10px. |
| `assets/panel.png` | 430×480 | Vertical parchment/wood menu panel with decorative carved border and corner rivets, plain center (menu buttons are drawn on top). |
| `assets/trophy.png` | 150×160 | A shiny gold trophy cup with a small sunflower engraved on it, confetti around. |
| `assets/defeat.png` | 220×160 | A comical zombie hand rising from disturbed earth giving a thumbs-up, small tombstone behind. Dark but funny, not gory. |

## 4. After generating — verify

```python
from PIL import Image
import os, numpy as np
spec = {
 'background_night.png':(1000,660,False),
 **{f'{n}.png':(90,100,True) for n in ['grave','sunshroom','sunshroom_big','puffshroom','fumeshroom','hypnoshroom','plantern']},
 'puff.png':(24,24,True), 'fume.png':(64,32,True),
 **{f'zombie_{n}.png':(110,140,True) for n in ['screendoor','dancer','backup']},
 'minibtn.png':(40,40,True), 'minibtn_active.png':(40,40,True),
 **{f'icon_{n}.png':(24,24,True) for n in ['pause','play','sound_on','sound_off']},
 'lock.png':(24,30,True), 'card.png':(100,124,True), 'panel.png':(430,480,True),
 'trophy.png':(150,160,True), 'defeat.png':(220,160,True),
}
for f,(w,h,rgba) in spec.items():
    p = os.path.join('assets', f)
    if not os.path.exists(p): print('MISSING', f); continue
    im = Image.open(p)
    ok = im.size==(w,h) and (not rgba or im.mode=='RGBA')
    # artwork must fill the canvas: opaque bounding box >= 88% of each dimension
    fill_ok = True
    if rgba and ok:
        a = np.asarray(im)[:,:,3]
        ys,xs = np.where(a>40)
        fill_ok = (xs.max()-xs.min())/w > .88 and (ys.max()-ys.min())/h > .88
    print('OK  ' if (ok and fill_ok) else f'BAD {im.size} {im.mode} fill_ok={fill_ok}', f)
```

24 files total. Regenerate any file that prints BAD (especially fill_ok=False — that means too much transparent padding). Do not modify `pvz.html` or existing assets.
