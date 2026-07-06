# Prompt for Codex — round 3 (new plants & zombies) — copy everything below this line

---

The game `pvz.html` loads art from `assets/` by exact filename. New gameplay was added and needs sprites. **Match the art style of the existing sprites in `assets/` exactly** (same painterly cartoon style, outlines, palette, lighting — open a few existing files for reference). Save every file into `assets/` with the exact filename and pixel dimensions below. PNG-24 RGBA, transparent background, no text/watermarks. Do not modify any existing file.

## Plants — 90×100 each, transparent, facing RIGHT (same framing as existing plant sprites)

| Filename | Description |
|---|---|
| `assets/squash.png` | A big grumpy yellow-green squash sitting on the grass, thick unibrow scowl, ready to pounce. Compact and heavy-looking. |
| `assets/jalapeno.png` | A furious red jalapeño pepper, slightly curved, steam/tiny flames coming off its head, gritted teeth, about to blow. |
| `assets/torchwood.png` | A friendly tree stump with bark texture and a warm face, with a steady campfire-like FLAME burning in a hollow on top. |
| `assets/tallnut.png` | Like the existing wall-nut but noticeably TALLER (fills the sprite vertically), stoic determined face, intact. |
| `assets/tallnut_cracked1.png` | Same tall-nut moderately damaged: cracks and chips, concerned face. |
| `assets/tallnut_cracked2.png` | Same tall-nut heavily damaged: deep cracks, chunks missing, a single tear, exhausted face. |

## Projectile — 24×24, transparent

| Filename | Description |
|---|---|
| `assets/firepea.png` | A blazing fire pea: orange-red glowing pea wrapped in flame with a small trailing fire wisp to the left. |

## Zombies — 110×140 each, transparent, facing LEFT, feet at bottom edge (same base zombie design as existing zombie sprites, vary only gear/pose)

| Filename | Description |
|---|---|
| `assets/zombie_polevault.png` | Zombie in a running pose holding a long bamboo/metal vaulting POLE diagonally, sporty torn tank top. |
| `assets/zombie_polevault_nopole.png` | The SAME zombie after his vault: no pole, normal walking pose, slightly winded expression. |
| `assets/zombie_football.png` | Bulky zombie in a red FOOTBALL HELMET with face mask and shoulder pads, charging head-down. |
| `assets/zombie_newspaper.png` | Zombie in boxers/robe shuffling while READING a grey newspaper held in front with both hands, reading glasses. |
| `assets/zombie_newspaper_angry.png` | The SAME zombie, newspaper gone: furious red-eyed sprint pose, mouth wide open, glasses askew. |
| `assets/zombie_jack.png` | Zombie carrying an orange JACK-IN-THE-BOX crank box against his chest, unsettling grin, the crank handle visible. |

## After generating — verify

```python
from PIL import Image
import os
spec = {
 **{f'{n}.png':(90,100) for n in ['squash','jalapeno','torchwood','tallnut','tallnut_cracked1','tallnut_cracked2']},
 'firepea.png':(24,24),
 **{f'zombie_{n}.png':(110,140) for n in ['polevault','polevault_nopole','football','newspaper','newspaper_angry','jack']},
}
for f,(w,h) in spec.items():
    p = os.path.join('assets', f)
    if not os.path.exists(p): print('MISSING', f); continue
    im = Image.open(p)
    print('OK  ' if (im.size==(w,h) and im.mode=='RGBA') else f'BAD {im.size} {im.mode}', f)
```

13 files total. Do not modify `pvz.html` or existing assets.
