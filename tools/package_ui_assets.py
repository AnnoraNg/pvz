from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
GEN = Path("/Users/admin/.codex/generated_images/019f31ef-30d9-7051-bb10-9a954cdfb0bd")

SOURCES = {
    "menu_background.png": GEN / "ig_0ce8c06242b73304016a4a72e77710819187c454a4ad321bfa.png",
    "logo.png": GEN / "ig_0ce8c06242b73304016a4a735b5ab08191850147525fc31a04.png",
    "hud_bar.png": GEN / "ig_0ce8c06242b73304016a4a73ab34208191b208b8f55eb44947.png",
    "sun_counter.png": GEN / "ig_0ce8c06242b73304016a4a73fac908819185113334f811c26c.png",
    "seed_packet.png": GEN / "ig_0ce8c06242b73304016a4a7485d0308191a56b43a858fcc8fb.png",
    "progress_frame.png": GEN / "ig_0ce8c06242b73304016a4a752a339081919e0cd4cef46da0ed.png",
    "progress_fill.png": GEN / "ig_0ce8c06242b73304016a4a759b4f5c81919e5ee45f848c41d8.png",
    "button.png": GEN / "ig_0e9fbe655a86b054016a4a7691da90819196b666addadeec46.png",
    "button_wide.png": GEN / "ig_0e9fbe655a86b054016a4a76f84a548191b1941f71de2c817d.png",
    "banner_ribbon.png": GEN / "ig_0e9fbe655a86b054016a4a77425fcc8191bce5d376c846e4be.png",
}

SIZES = {
    "menu_background.png": (1000, 660),
    "logo.png": (640, 280),
    "hud_bar.png": (980, 100),
    "sun_counter.png": (110, 86),
    "seed_packet.png": (68, 86),
    "progress_frame.png": (300, 36),
    "progress_fill.png": (280, 16),
    "button.png": (220, 60),
    "button_wide.png": (460, 56),
    "banner_ribbon.png": (720, 100),
}


def remove_magenta(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if r > 180 and b > 145 and g < 100:
                px[x, y] = (r, g, b, 0)
            elif r > 140 and b > 110 and g < 135 and (r + b) > g * 3:
                px[x, y] = (r, g, b, max(0, min(a, (g - 35) * 3)))
    alpha = im.getchannel("A").filter(ImageFilter.MedianFilter(3)).filter(ImageFilter.GaussianBlur(0.25))
    im.putalpha(alpha)
    return im


def crop_to_content(im: Image.Image) -> Image.Image:
    bbox = im.getbbox()
    return im.crop(bbox) if bbox else im


def fit_transparent(im: Image.Image, size: tuple[int, int], fill=0.94) -> Image.Image:
    im = crop_to_content(remove_magenta(im))
    max_w = int(size[0] * fill)
    max_h = int(size[1] * fill)
    scale = min(max_w / im.width, max_h / im.height)
    im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
    out = Image.new("RGBA", size, (0, 0, 0, 0))
    out.alpha_composite(im, ((size[0] - im.width) // 2, (size[1] - im.height) // 2))
    return out


def crop_resize_opaque(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    im = im.convert("RGB")
    src_ratio = im.width / im.height
    dst_ratio = size[0] / size[1]
    if src_ratio > dst_ratio:
        new_w = int(im.height * dst_ratio)
        x = (im.width - new_w) // 2
        im = im.crop((x, 0, x + new_w, im.height))
    else:
        new_h = int(im.width / dst_ratio)
        y = (im.height - new_h) // 2
        im = im.crop((0, y, im.width, y + new_h))
    return im.resize(size, Image.Resampling.LANCZOS)


def progress_fill(im: Image.Image) -> Image.Image:
    # Use the generated gel texture, then normalize it into the exact opaque strip.
    im = crop_resize_opaque(im, SIZES["progress_fill.png"]).convert("RGBA")
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle((0, 0, 279, 3), fill=(186, 255, 101, 120))
    d.rectangle((254, 0, 279, 15), fill=(17, 117, 31, 55))
    return im.convert("RGB")


def progress_frame(im: Image.Image) -> Image.Image:
    out = fit_transparent(im, SIZES["progress_frame.png"], fill=0.98)
    # Hard requirement: inner transparent window exactly 280x16, centered.
    alpha = out.getchannel("A")
    d = ImageDraw.Draw(alpha)
    d.rectangle((10, 10, 289, 25), fill=0)
    out.putalpha(alpha)
    return out


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for name, src in SOURCES.items():
        im = Image.open(src)
        if name == "menu_background.png":
            out = crop_resize_opaque(im, SIZES[name])
        elif name == "progress_fill.png":
            out = progress_fill(im)
        elif name == "progress_frame.png":
            out = progress_frame(im)
        elif name == "logo.png":
            out = fit_transparent(im, SIZES[name], fill=0.98)
        else:
            out = fit_transparent(im, SIZES[name], fill=0.96)
        out.save(ASSETS / name)


if __name__ == "__main__":
    main()
