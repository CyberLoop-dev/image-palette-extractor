#!/usr/bin/env python3
"""Extract dominant colors from an image and export CSS or JSON."""
import argparse
import json
from pathlib import Path
from PIL import Image


def extract_palette(source: Path, count: int) -> list[dict]:
    with Image.open(source) as original:
        image = original.convert("RGB")
        image.thumbnail((400, 400))
        quantized = image.quantize(colors=count, method=Image.Quantize.MEDIANCUT)
        palette = quantized.getpalette() or []
        histogram = quantized.getcolors() or []
        items = []
        for pixels, index in sorted(histogram, reverse=True):
            offset = index * 3
            rgb = palette[offset:offset + 3]
            if len(rgb) == 3:
                items.append({"hex": "#{:02X}{:02X}{:02X}".format(*rgb), "pixels": pixels})
        return items[:count]


def render_css(colors: list[dict]) -> str:
    lines = [":root {"]
    for index, item in enumerate(colors, 1):
        lines.append(f"  --palette-{index}: {item['hex']};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--colors", type=int, default=6)
    parser.add_argument("--format", choices=("css", "json"), default="css")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not args.image.is_file():
        parser.error(f"image not found: {args.image}")
    if not 2 <= args.colors <= 32:
        parser.error("--colors must be between 2 and 32")
    try:
        palette = extract_palette(args.image, args.colors)
        result = render_css(palette) if args.format == "css" else json.dumps(palette, indent=2) + "\n"
        if args.output:
            args.output.write_text(result, encoding="utf-8")
            print(f"Wrote {len(palette)} colors -> {args.output}")
        else:
            print(result, end="")
        return 0
    except OSError as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
