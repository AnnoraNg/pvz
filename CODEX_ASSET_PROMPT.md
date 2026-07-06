# Prompt for Codex — copy everything below this line

---

Generate a complete set of game art assets (PNG images) for an HTML5 canvas tower-defense game in the style of Plants vs. Zombies. The game file `pvz.html` already exists in this folder and automatically loads sprites from an `assets/` subfolder by exact filename — **create the folder `assets/` next to `pvz.html` and save every image there with the exact filename and exact pixel dimensions listed below.** If a filename or dimension is wrong, the game silently falls back to placeholder vector art, so treat the spec as strict.

## Global art style (applies to every image)

- Cartoon style with bold dark outlines (~3px), vibrant saturated colors, soft cel shading with light coming from the top-left. Cheerful, slightly goofy tone — plants look cute and determined, zombies look dopey and shabby, not scary or gory.
- Original artwork **inspired by** the tower-defense lawn genre — do NOT copy or trace actual Plants vs. Zombies characters or assets.
- All sprites (everything except `background.png`): PNG-24 with a fully transparent background (alpha channel). No baked-in drop shadows, no ground shadow, no background color, no text or watermarks.
- Consistent palette and rendering style across ALL images so they look like one game.
- The subject should fill ~85–90% of the canvas with a few pixels of transparent padding; keep it centered horizontally.
- Exact pixel dimensions are mandatory. If your generation tool outputs a different size, resize/crop to spec before saving.

## Facing directions (critical)

- **Plants face RIGHT** (they shoot toward the right side of the screen).
- **Zombies face LEFT** (they walk from right to left).

## 1. Background — `assets/background.png` — 1000×660

A single daytime front-lawn scene. The game draws everything else on top, so this is scenery only (no characters, no UI). Layout must match these exact pixel coordinates:

- **x 0–130 (left edge):** the side of a cozy suburban house — brick/wood wall with a few windows, extending from y≈120 down to the bottom. Above y≈120 it can be sky.
- **y 0–110 (top strip):** blue sky with a couple of soft clouds. (The game draws a HUD bar over y 0–115, so keep this area simple.)
- **Lawn grid:** starts at x=130, y=140. Exactly **9 columns × 92px wide** and **5 rows × 98px tall** (so the grid spans x 130→958, y 140→630). Render it as a checkerboard of two greens — a cell at column c, row r is the LIGHTER green (#69a83f) when (r+c) is even, and the DARKER green (#5c9636) when (r+c) is odd. Column/row boundaries must land exactly on the 92/98px steps because the game places plants by grid cell. Subtle grass texture inside cells is fine; keep the two-tone checkerboard clearly visible.
- **x 958–1000 (right edge):** a dirt/road strip where zombies enter — brown earth, maybe a broken fence hint.
- **y 630–660 (bottom strip):** darker grass/soil edge below the lawn.

## 2. Plants — each exactly **90×100**, transparent PNG, facing right

The visual "body" should sit in the lower ~80% of the canvas (these are drawn anchored to a lawn cell; leave the top ~10px mostly empty except for tall details).

| Filename | Description |
|---|---|
| `assets/sunflower.png` | Smiling sunflower: brown center face with happy eyes, ring of bright yellow petals, green stem and two leaves. |
| `assets/peashooter.png` | Green plant with a round head and a wide tubular snout pointing RIGHT, on a stem with leaves. Determined face. |
| `assets/snowpea.png` | Same body plan as the peashooter but icy blue/cyan, with small icicles hanging from its snout and a frosty sheen. |
| `assets/repeater.png` | Like the peashooter but darker green and with TWO snouts pointing right (one behind the other), looks tougher/angrier. |
| `assets/wallnut.png` | Big tan-brown walnut with a calm smiling face, sitting on the grass. Intact, no damage. |
| `assets/wallnut_cracked1.png` | The SAME walnut but moderately damaged: a few visible cracks, chipped top, worried expression. |
| `assets/wallnut_cracked2.png` | The SAME walnut heavily damaged: large deep cracks, chunks missing, exhausted/grimacing face. |
| `assets/cherrybomb.png` | Two glossy red cherries joined by a green stem, with angry lit-fuse expressions; tiny spark on the stem. |
| `assets/potatomine_buried.png` | Mostly-buried potato: just a small mound of dirt with the top of a potato and a tiny green sprout antenna peeking out. Low to the ground (bottom third of canvas). |
| `assets/potatomine_armed.png` | The potato now fully surfaced: round tan potato with eyes and a glowing RED light/antenna on top, sitting on the dirt mound. |
| `assets/chomper.png` | Purple Venus-flytrap-style plant with big open jaws (spiky teeth) facing RIGHT on a thick green stem, hungry expression. |
| `assets/chomper_chewing.png` | The same chomper but with jaws clamped SHUT and cheeks bulging, mid-chew, content expression. |

## 3. Zombies — each exactly **110×140**, transparent PNG, facing left

Full body, feet at the very bottom edge of the canvas (the game anchors sprites by the bottom). Mid-stride walking pose, arms reaching forward (to the LEFT). Grey-green skin, tattered brown/grey suit, vacant dopey expression. Keep the same base zombie design across all five and vary only the headwear/props:

| Filename | Description |
|---|---|
| `assets/zombie_normal.png` | The base zombie: no headwear, messy hair, torn tie. |
| `assets/zombie_cone.png` | Same zombie wearing a battered ORANGE traffic cone on his head. |
| `assets/zombie_bucket.png` | Same zombie wearing a dented METAL BUCKET on his head, covering to eyebrow level. |
| `assets/zombie_flag.png` | Same zombie holding a tall pole with a tattered RED flag (flag points right/behind him), marching pose, slightly more energetic. |
| `assets/zombie_runner.png` | A leaner, sportier zombie in a running pose: red headband, jogging shorts/tracksuit hints, one foot off the ground, leaning forward. |

## 4. Effects & UI

| Filename | Size | Description |
|---|---|---|
| `assets/sun.png` | 60×60 | A radiant collectible sun: bright yellow-orange glowing orb with soft rays, slight outer glow fading to transparent. |
| `assets/pea.png` | 24×24 | A single glossy green pea projectile with a small highlight. |
| `assets/frozenpea.png` | 24×24 | An icy light-blue pea with frost sparkle and a tiny trailing chill mist. |
| `assets/mower.png` | 64×60 | A small red push lawnmower seen from the side, facing RIGHT, dark wheels, silver handle. |
| `assets/shovel.png` | 48×72 | A garden shovel, blade at the bottom, wooden handle at the top, upright, slight diagonal tilt. |

## 5. After generating — verify

Run this check and fix any mismatch (regenerate or resize) until it prints all OK:

```python
from PIL import Image
import os
spec = {
 'background.png':(1000,660),'sun.png':(60,60),'pea.png':(24,24),'frozenpea.png':(24,24),
 'mower.png':(64,60),'shovel.png':(48,72),
 **{f'{n}.png':(90,100) for n in ['sunflower','peashooter','snowpea','repeater','wallnut',
   'wallnut_cracked1','wallnut_cracked2','cherrybomb','potatomine_buried','potatomine_armed',
   'chomper','chomper_chewing']},
 **{f'zombie_{n}.png':(110,140) for n in ['normal','cone','bucket','flag','runner']},
}
for f,(w,h) in spec.items():
    p = os.path.join('assets',f)
    if not os.path.exists(p): print('MISSING', f); continue
    im = Image.open(p)
    ok = im.size==(w,h) and (f=='background.png' or im.mode=='RGBA')
    print('OK  ' if ok else f'BAD {im.size} {im.mode}', f)
```

All sprites except the background must be mode RGBA (transparent). 23 files total. Do not modify `pvz.html`.
