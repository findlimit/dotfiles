#!/usr/bin/env python3
import os
import json
import argparse
import re

def hex_to_rgba_components(hex_str: str):
    """
    Convert a hex color string to integer RGBA components (0–255).
    Accepts:
      - RRGGBB
      - AARRGGBB (alpha first)
      - #RRGGBB or #AARRGGBB
      - 0xRRGGBB or 0xAARRGGBB (case-insensitive)
    Returns (r, g, b, a).
    """
    s = hex_str.strip()
    # strip 0x/0X or #
    if s.lower().startswith("0x"):
        s = s[2:]
    elif s.startswith("#"):
        s = s[1:]
    # now must be 6 or 8 hex digits
    if not re.fullmatch(r"[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8}", s):
        raise ValueError(f"Invalid hex color: {hex_str}")
    # parse components
    if len(s) == 8:
        a = int(s[0:2], 16)
        r = int(s[2:4], 16)
        g = int(s[4:6], 16)
        b = int(s[6:8], 16)
    else:
        a = 0xFF
        r = int(s[0:2], 16)
        g = int(s[2:4], 16)
        b = int(s[4:6], 16)
    return r, g, b, a

def generate_color_assets(palette: dict, out_dir: str):
    """Generate an .xcassets folder with a .colorset for each named color."""
    os.makedirs(out_dir, exist_ok=True)

    for name, hexval in palette.items():
        r, g, b, a = hex_to_rgba_components(hexval)

        colorset_dir = os.path.join(out_dir, f"{name}.colorset")
        os.makedirs(colorset_dir, exist_ok=True)

        content = {
            "colors": [
                {
                    "color": {
                        "color-space": "srgb",
                        "components": {
                            "red":   f"0x{r:02X}",
                            "green": f"0x{g:02X}",
                            "blue":  f"0x{b:02X}",
                            "alpha": f"{a/255:.3f}"
                        }
                    },
                    "idiom": "universal"
                },
                {
                    "appearances": [
                        {
                            "appearance": "luminosity",
                            "value": "dark"
                        }
                    ],
                    "color": {
                        "color-space": "srgb",
                        "components": {
                            "red":   f"0x{r:02X}",
                            "green": f"0x{g:02X}",
                            "blue":  f"0x{b:02X}",
                            "alpha": f"{a/255:.3f}"
                        }
                    },
                    "idiom": "universal"
                }
            ],
            "info": {
                "version": 1,
                "author": "xcode"
            }
        }

        with open(os.path.join(colorset_dir, "Contents.json"), "w") as f:
            json.dump(content, f, indent=2)

    print(f"✅ Generated color assets in {out_dir}/")

def main():
    parser = argparse.ArgumentParser(
        description="Generate Xcode .xcassets color sets from a JSON palette file."
    )
    parser.add_argument(
        "json_path",
        help="Path to JSON file mapping color names to hex values, e.g. {\"Primary\": \"0xAARRGGBB\", …}"
    )
    parser.add_argument(
        "-o", "--output",
        default="Assets.xcassets",
        help="Output .xcassets directory (default: Assets.xcassets)"
    )
    args = parser.parse_args()

    try:
        with open(args.json_path, "r") as f:
            palette = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        parser.exit(1)

    if not isinstance(palette, dict):
        print("Error: JSON must be an object mapping names to hex strings.")
        parser.exit(1)

    generate_color_assets(palette, args.output)

if __name__ == "__main__":
    main()
