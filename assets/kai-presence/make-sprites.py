import sys
from pathlib import Path
from PIL import Image, ImageDraw

SRC_DIR = Path(__file__).parent
OUT_DIR = SRC_DIR / "sprites"
EXPRS = ["calma", "chave", "furia", "leitura", "sono", "sorriso", "pensando"]
SIZES = {"sm": 140, "md": 200, "lg": 260}
CHROMA = (16, 20, 28)
CROP_TOP = 30
CARD_RATIO = 1.25
RADIUS_PCT = 0.12


def rounded_mask(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=r, fill=255)
    return m


def make_card(expr, width):
    src = Image.open(SRC_DIR / f"kai-expr-{expr}.png").convert("RGB")
    sw, sh = src.size
    ch = int(sw * CARD_RATIO)
    if CROP_TOP + ch > sh:
        ch = sh - CROP_TOP
    crop = src.crop((0, CROP_TOP, sw, CROP_TOP + ch))
    height = int(width * CARD_RATIO)
    art = crop.resize((width, height), Image.LANCZOS)
    r = max(6, int(width * RADIUS_PCT))
    card = Image.new("RGB", (width, height), CHROMA)
    card.paste(art, (0, 0), rounded_mask(width, height, r))
    return card.convert("RGB")


def main():
    total = 0
    for tag, w in SIZES.items():
        d = OUT_DIR / tag
        d.mkdir(parents=True, exist_ok=True)
        for expr in EXPRS:
            img = make_card(expr, w)
            img.save(d / f"kai-spr-{expr}.png", optimize=True)
            total += 1
    print(f"OK: {total} sprites gerados em {OUT_DIR}")


if __name__ == "__main__":
    sys.exit(main())
