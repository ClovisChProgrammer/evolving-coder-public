#!/usr/bin/env python3
"""Gera frames de animação aplicando transformações sutis aos sprites base."""
from pathlib import Path
from PIL import Image, ImageFilter
import math

import sys

SIZE = sys.argv[1] if len(sys.argv) > 1 else "md"
SPRITES_DIR = Path(__file__).parent.parent / "assets" / "kai-presence" / "sprites" / SIZE
OUT_DIR = SPRITES_DIR

# Mapeamento: estado -> (arquivo_base, estilo_animacao)
ANIM_SPECS = {
    "calma":       ("kai-spr-calma.png",       "breathing"),      # idle
    "pensando":    ("kai-spr-pensando.png",    "head_tilt"),      # thinking
    "chave":       ("kai-spr-chave.png",       "bounce"),         # working
    "sorriso":     ("kai-spr-sorriso.png",     "mouth"),          # speaking + milestone
    "furia":       ("kai-spr-furia.png",       "shake"),          # error
    "sono":        ("kai-spr-sono.png",        "slow_breath"),    # shutdown
    "leitura":     ("kai-spr-leitura.png",     "head_tilt"),      # reading
}

FRAMES_PER_STATE = 4

def breathing(img, frame, total):
    """Respiração suave: escala vertical 1.0 -> 1.02 -> 1.0 -> 0.98"""
    phase = (frame / (total - 1)) * 2 * math.pi
    scale_y = 1.0 + 0.02 * math.sin(phase)
    w, h = img.size
    new_h = int(h * scale_y)
    return img.resize((w, new_h), Image.LANCZOS)

def head_tilt(img, frame, total):
    """Inclinação leve da cabeça: -3° -> +3° -> -3°"""
    angle = 3 * math.sin((frame / (total - 1)) * 2 * math.pi)
    return img.rotate(angle, resample=Image.BICUBIC, expand=False, fillcolor=(0,0,0,0))

def bounce(img, frame, total):
    """Pulo sutil: translação Y -2 -> +2 -> -2 px"""
    offset_y = int(2 * math.sin((frame / (total - 1)) * 2 * math.pi))
    w, h = img.size
    canvas = Image.new("RGBA", (w, h + 4), (0,0,0,0))
    canvas.paste(img, (0, 2 + offset_y), img)
    return canvas.crop((0, 2, w, h + 2))

def mouth(img, frame, total):
    """Abertura de boca: escala Y da metade inferior 1.0 -> 1.08 -> 1.0"""
    phase = (frame / (total - 1)) * 2 * math.pi
    scale = 1.0 + 0.08 * max(0, math.sin(phase))
    w, h = img.size
    mid = h // 2
    top = img.crop((0, 0, w, mid))
    bottom = img.crop((0, mid, w, h))
    new_bottom_h = int(bottom.height * scale)
    bottom = bottom.resize((w, new_bottom_h), Image.LANCZOS)
    canvas = Image.new("RGBA", (w, mid + new_bottom_h), (0,0,0,0))
    canvas.paste(top, (0, 0))
    canvas.paste(bottom, (0, mid), bottom)
    return canvas

def shake(img, frame, total):
    """Tremor: jitter aleatório pequeno"""
    import random
    random.seed(frame * 1337)
    dx = random.randint(-2, 2)
    dy = random.randint(-2, 2)
    w, h = img.size
    canvas = Image.new("RGBA", (w + 4, h + 4), (0,0,0,0))
    canvas.paste(img, (2 + dx, 2 + dy), img)
    return canvas.crop((2, 2, w + 2, h + 2))

def slow_breath(img, frame, total):
    """Respiração lenta: escala 1.0 -> 1.015 -> 1.0 -> 0.985"""
    phase = (frame / (total - 1)) * 2 * math.pi
    scale = 1.0 + 0.015 * math.sin(phase)
    w, h = img.size
    new_w, new_h = int(w * scale), int(h * scale)
    resized = img.resize((new_w, new_h), Image.LANCZOS)
    canvas = Image.new("RGBA", (w, h), (0,0,0,0))
    canvas.paste(resized, ((w - new_w)//2, (h - new_h)//2), resized)
    return canvas

STYLE_FUNCS = {
    "breathing": breathing,
    "slow_breath": slow_breath,
    "head_tilt": head_tilt,
    "bounce": bounce,
    "mouth": mouth,
    "shake": shake,
}

def main():
    print(f"Gerando frames em {OUT_DIR}")
    for state, (base_file, style) in ANIM_SPECS.items():
        base_path = SPRITES_DIR / base_file
        if not base_path.exists():
            print(f"  ⚠ Base não encontrada: {base_file}")
            continue
        base_img = Image.open(base_path).convert("RGBA")
        func = STYLE_FUNCS[style]
        for i in range(1, FRAMES_PER_STATE + 1):
            frame_img = func(base_img, i - 1, FRAMES_PER_STATE)
            out_name = base_file.replace(".png", f"-{i}.png")
            out_path = OUT_DIR / out_name
            frame_img.save(out_path, "PNG")
            print(f"  OK {out_name}")
    print("Concluido!")

if __name__ == "__main__":
    main()