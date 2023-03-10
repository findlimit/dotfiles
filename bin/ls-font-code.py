#!/usr/local/bin/python3

import argparse
from fontTools.ttLib import TTFont

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('font_path', help='Path to the font file')
args = parser.parse_args()

# Open the font file
font = TTFont(args.font_path)

# Get the list of Unicode characters that are available in the font
characters = font['cmap'].getBestCmap().keys()

# Print the list of characters
for character in characters:
    print(format(character, "x"), end=",")

