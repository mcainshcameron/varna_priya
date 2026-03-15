#!/usr/bin/env python3
"""
Varna Priya — image processing utility.
Usage: python3 _process_image.py <type> <input_path> <output_path> [width] [height]

Types:
  blog_featured     → 1200x675 JPEG 80%
  blog_content      → max_width 1000 JPEG 75%
  mandala_display   → 800x800 JPEG 75%  (fit inside, pad transparent)
  mandala_original  → copy as PNG (no downscale)
  craft_display     → 800x600 JPEG 75%
  wallpaper_display → 800x450 JPEG 75%
  resource_preview  → 400x300 JPEG 75%
  hero              → 1200x1200 JPEG 85%
  custom            → width height JPEG 80%
"""

import sys
import os
from PIL import Image, ImageOps

CONFIGS = {
    "blog_featured":     {"size": (1200, 675),  "format": "JPEG", "quality": 80,  "mode": "cover"},
    "blog_content":      {"size": (1000, 9999),  "format": "JPEG", "quality": 75,  "mode": "width"},
    "mandala_display":   {"size": (800, 800),    "format": "JPEG", "quality": 75,  "mode": "fit"},
    "mandala_original":  {"size": None,          "format": "PNG",  "quality": 100, "mode": "copy"},
    "craft_display":     {"size": (800, 600),    "format": "JPEG", "quality": 75,  "mode": "cover"},
    "wallpaper_display": {"size": (800, 450),    "format": "JPEG", "quality": 75,  "mode": "cover"},
    "resource_preview":  {"size": (400, 300),    "format": "JPEG", "quality": 75,  "mode": "cover"},
    "hero":              {"size": (1200, 1200),  "format": "JPEG", "quality": 85,  "mode": "cover"},
}


def process(img_type, input_path, output_path, custom_w=None, custom_h=None):
    if img_type == "custom":
        cfg = {"size": (int(custom_w), int(custom_h)), "format": "JPEG", "quality": 80, "mode": "cover"}
    else:
        cfg = CONFIGS.get(img_type)
        if not cfg:
            print(f"Unknown type: {img_type}")
            sys.exit(1)

    img = Image.open(input_path)

    # Ensure RGB for JPEG output
    if cfg["format"] == "JPEG" and img.mode in ("RGBA", "P", "LA"):
        background = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        background.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
        img = background
    elif cfg["format"] == "JPEG" and img.mode != "RGB":
        img = img.convert("RGB")

    if cfg["mode"] == "copy":
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        img.save(output_path, format=cfg["format"])
        print(f"Copied → {output_path}")
        return

    target_w, target_h = cfg["size"]

    if cfg["mode"] == "cover":
        img = ImageOps.fit(img, (target_w, target_h), method=Image.LANCZOS)
    elif cfg["mode"] == "fit":
        img.thumbnail((target_w, target_h), Image.LANCZOS)
    elif cfg["mode"] == "width":
        if img.width > target_w:
            ratio = target_w / img.width
            img = img.resize((target_w, int(img.height * ratio)), Image.LANCZOS)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    save_kwargs = {"format": cfg["format"]}
    if cfg["format"] == "JPEG":
        save_kwargs["quality"] = cfg["quality"]
        save_kwargs["optimize"] = True
    img.save(output_path, **save_kwargs)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"Saved {img.width}x{img.height} @ {size_kb:.0f}KB → {output_path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        print(__doc__)
        sys.exit(1)
    process(*args)
