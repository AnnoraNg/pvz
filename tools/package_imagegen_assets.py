from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
GEN = Path("/Users/admin/.codex/generated_images")


SOURCES = {
    "background.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_05becd4de39c2846016a4a3c379cb08191bdd77c1389b50fd1.png",
    "sunflower.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3c9fe2f48191a4418626caa552ea.png",
    "peashooter.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3cf70d8c8191bb69b62d2ed2f44f.png",
    "snowpea.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3d73153081918c4c279bea04340e.png",
    "repeater.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3dd0261481918f7d7f1b7eda11b3.png",
    "wallnut.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3e39f6fc81918e6dbe90af816bd5.png",
    "wallnut_cracked1.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3e9ef2dc819191b6738b091e455e.png",
    "wallnut_cracked2.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3f31fe948191bc9b57e3d647fa55.png",
    "cherrybomb.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a3f9eecf881919a2ebda9432584d8.png",
    "potatomine_buried.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a400bf06c81919596bb74e42236fc.png",
    "potatomine_armed.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a40506aa88191bcaf5a1d0aceb716.png",
    "chomper.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a40a8c7348191bd3d622bef6e7842.png",
    "chomper_chewing.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a4116db9481918a3ed65d5d2a8905.png",
    "zombie_normal.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a417aa268819182884a8a855f74d3.png",
    "zombie_cone.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a41ddaa7c8191b0fd713a39c4bf8e.png",
    "zombie_bucket.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a422af06c8191bf77cd002f5917de.png",
    "zombie_flag.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a42764f9c8191b7939d0152d5373d.png",
    "zombie_runner.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a42dbcee88191b8aa430467104810.png",
    "sun.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a434f21808191a263c686e5617bb1.png",
    "pea.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a438529d4819196dc64c2a5a44e0e.png",
    "frozenpea.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a43db57b88191830cd38fdf74904c.png",
    "mower.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a4429b9a08191ba333a6ee7e69c4b.png",
    "shovel.png": "019f31ef-30d9-7051-bb10-9a954cdfb0bd/ig_0a62e1dde3404184016a4a44805b148191a147816b2b049253.png",
}

SIZES = {
    "background.png": (1000, 660),
    "sun.png": (60, 60),
    "pea.png": (24, 24),
    "frozenpea.png": (24, 24),
    "mower.png": (64, 60),
    "shovel.png": (48, 72),
    **{f"{name}.png": (90, 100) for name in [
        "sunflower",
        "peashooter",
        "snowpea",
        "repeater",
        "wallnut",
        "wallnut_cracked1",
        "wallnut_cracked2",
        "cherrybomb",
        "potatomine_buried",
        "potatomine_armed",
        "chomper",
        "chomper_chewing",
    ]},
    **{f"zombie_{name}.png": (110, 140) for name in ["normal", "cone", "bucket", "flag", "runner"]},
}


def remove_magenta(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if r > 180 and b > 150 and g < 95:
                px[x, y] = (r, g, b, 0)
            elif r > 140 and b > 115 and g < 135 and r + b > g * 3:
                alpha = max(0, min(a, int((g - 35) * 3)))
                px[x, y] = (r, g, b, alpha)
    alpha = im.getchannel("A").filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(0.35))
    im.putalpha(alpha)
    return im


def fit_sprite(im: Image.Image, size: tuple[int, int], low: bool = False) -> Image.Image:
    im = remove_magenta(im)
    bbox = im.getbbox()
    if not bbox:
        return Image.new("RGBA", size, (0, 0, 0, 0))
    im = im.crop(bbox)
    max_w = int(size[0] * (0.90 if size[0] > 30 else 0.82))
    max_h = int(size[1] * (0.90 if size[1] > 30 else 0.82))
    scale = min(max_w / im.width, max_h / im.height)
    new_size = (max(1, int(im.width * scale)), max(1, int(im.height * scale)))
    im = im.resize(new_size, Image.Resampling.LANCZOS)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    x = (size[0] - im.width) // 2
    y = size[1] - im.height if low else (size[1] - im.height) // 2
    if size[1] >= 100:
        y = size[1] - im.height
    out.alpha_composite(im, (x, y))
    return out


def exact_background(src: Image.Image) -> Image.Image:
    src = src.convert("RGB")
    w, h = src.size
    target_ratio = 1000 / 660
    if w / h > target_ratio:
        nw = int(h * target_ratio)
        x = (w - nw) // 2
        src = src.crop((x, 0, x + nw, h))
    else:
        nh = int(w / target_ratio)
        y = (h - nh) // 2
        src = src.crop((0, y, w, y + nh))
    out = src.resize((1000, 660), Image.Resampling.LANCZOS).convert("RGBA")
    d = ImageDraw.Draw(out, "RGBA")

    # Keep the generated image's painterly edges, but enforce the game-critical
    # board geometry so plant placement lines up with the existing canvas code.
    d.rectangle((0, 0, 1000, 115), fill=(116, 199, 249, 230))
    d.rectangle((0, 120, 130, 660), fill=(177, 102, 61, 235))
    for y in range(140, 650, 38):
        d.line((0, y, 130, y), fill=(119, 64, 43, 180), width=1)
    for x in range(0, 130, 42):
        d.line((x, 120, x, 660), fill=(119, 64, 43, 180), width=1)
    d.rounded_rectangle((27, 180, 97, 253), radius=7, fill=(150, 220, 242, 245), outline=(76, 48, 33, 255), width=3)
    d.line((62, 183, 62, 250), fill=(76, 48, 33, 255), width=3)
    d.line((30, 218, 94, 218), fill=(76, 48, 33, 255), width=3)

    for r in range(5):
        for c in range(9):
            color = (105, 168, 63, 238) if (r + c) % 2 == 0 else (92, 150, 54, 238)
            x0, y0 = 130 + c * 92, 140 + r * 98
            d.rectangle((x0, y0, x0 + 92, y0 + 98), fill=color)
            for i in range(9):
                gx = x0 + 8 + ((i * 17 + r * 13 + c * 7) % 76)
                gy = y0 + 10 + ((i * 19 + r * 11 + c * 5) % 78)
                d.arc((gx, gy, gx + 10, gy + 12), 215, 315, fill=(37, 88, 31, 80), width=1)
            exact = (105, 168, 63, 255) if (r + c) % 2 == 0 else (92, 150, 54, 255)
            d.rectangle((x0 + 43, y0 + 46, x0 + 49, y0 + 52), fill=exact)
    for c in range(10):
        x = 130 + c * 92
        d.line((x, 140, x, 630), fill=(48, 99, 33, 95), width=1)
    for r in range(6):
        y = 140 + r * 98
        d.line((130, y, 958, y), fill=(48, 99, 33, 95), width=1)
    d.rectangle((958, 110, 1000, 660), fill=(133, 91, 45, 245))
    d.rectangle((130, 630, 1000, 660), fill=(55, 104, 39, 245))
    return out.convert("RGB")


def main():
    ASSETS.mkdir(exist_ok=True)
    for old in ASSETS.glob("*.png"):
        old.unlink()
    for name, rel in SOURCES.items():
        src = Image.open(GEN / rel)
        size = SIZES[name]
        if name == "background.png":
            out = exact_background(src)
        else:
            out = fit_sprite(src, size, low=name == "potatomine_buried.png")
        out.save(ASSETS / name)


if __name__ == "__main__":
    main()
