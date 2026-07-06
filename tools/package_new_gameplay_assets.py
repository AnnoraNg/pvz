from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
GEN = Path("/Users/admin/.codex/generated_images/019f31ef-30d9-7051-bb10-9a954cdfb0bd")

SOURCES = {
    "squash.png": GEN / "ig_075b7a7daa1eeb46016a4b0ec684e88191b4bc7248200a3494.png",
    "jalapeno.png": GEN / "ig_075b7a7daa1eeb46016a4b0f23b5b8819193d0f406eb5ba5cf.png",
    "torchwood.png": GEN / "ig_075b7a7daa1eeb46016a4b0f74c1c48191939d5f237d8669b6.png",
    "tallnut.png": GEN / "ig_075b7a7daa1eeb46016a4b0fb8151c81918f0a3bc4eb4903bc.png",
    "tallnut_cracked1.png": GEN / "ig_075b7a7daa1eeb46016a4b101520c8819191480c6aaed576f2.png",
    "tallnut_cracked2.png": GEN / "ig_075b7a7daa1eeb46016a4b1071e1e481918418f2eded198d68.png",
    "firepea.png": GEN / "ig_075b7a7daa1eeb46016a4b10dd8b888191b32bfdb71751c950.png",
    "zombie_polevault.png": GEN / "ig_075b7a7daa1eeb46016a4b112492bc819180dbf3b97cdeadd8.png",
    "zombie_polevault_nopole.png": GEN / "ig_075b7a7daa1eeb46016a4b118129508191a314dbfa883ae03a.png",
    "zombie_football.png": GEN / "ig_00e05e135aee7102016a4b12609b2c8191897122e6db3de870.png",
    "zombie_newspaper.png": GEN / "ig_00e05e135aee7102016a4b12d7834c8191b938ebb91a92347d.png",
    "zombie_newspaper_angry.png": GEN / "ig_00e05e135aee7102016a4b13328cb08191819f69bbbadcb126.png",
    "zombie_jack.png": GEN / "ig_00e05e135aee7102016a4b1394e4e081919a7456e2b273df9a.png",
}

SIZES = {
    **{f"{n}.png": (90, 100) for n in ["squash", "jalapeno", "torchwood", "tallnut", "tallnut_cracked1", "tallnut_cracked2"]},
    "firepea.png": (24, 24),
    **{f"zombie_{n}.png": (110, 140) for n in ["polevault", "polevault_nopole", "football", "newspaper", "newspaper_angry", "jack"]},
}


def remove_magenta(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if r > 180 and b > 145 and g < 100:
                px[x, y] = (r, g, b, 0)
            elif r > 135 and b > 110 and g < 145 and (r + b) > g * 3:
                px[x, y] = (r, g, b, max(0, min(a, int((g - 35) * 3))))
    alpha = im.getchannel("A").filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(0.25))
    im.putalpha(alpha)
    return im


def fit_sprite(im: Image.Image, size: tuple[int, int], fill: float = 0.9, bottom_anchor: bool = True) -> Image.Image:
    im = remove_magenta(im)
    bbox = im.getbbox()
    if not bbox:
        return Image.new("RGBA", size, (0, 0, 0, 0))
    im = im.crop(bbox)
    max_w = int(size[0] * fill)
    max_h = int(size[1] * fill)
    scale = min(max_w / im.width, max_h / im.height)
    im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    x = (size[0] - im.width) // 2
    y = size[1] - im.height if bottom_anchor else (size[1] - im.height) // 2
    out.alpha_composite(im, (x, y))
    return out


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for name, src in SOURCES.items():
        size = SIZES[name]
        fill = 0.84 if name == "firepea.png" else 0.9
        out = fit_sprite(Image.open(src), size, fill=fill, bottom_anchor=name != "firepea.png")
        out.save(ASSETS / name)


if __name__ == "__main__":
    main()
