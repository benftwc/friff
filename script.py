#!/usr/bin/env python3
# Imports
import argparse
import os

from PIL import Image

from lib.helpers import get_random_name
from lib.screenshot import generate_screenshot, pixel_diffs

# Prepare Arguments Parser
parser = argparse.ArgumentParser(
    description="Take screenshot and compare them to get differences between two given environments"
)
parser.add_argument(
    "-s",
    "--source",
    metavar="URL",
    dest="source_url",
    help="The source website URL",
)
parser.add_argument(
    "-t",
    "--target",
    metavar="URL",
    dest="target_url",
    help="The target website URL",
)
parser.add_argument(
    "-k",
    "--keep-files",
    dest="keep_files",
    default=False,
    help="Keep files after comparison",
    action="store_true",
)
parser.add_argument(
    "-p",
    "--purge-files",
    dest="purge_files",
    default=False,
    help="Remove files before take screenshots",
    action="store_true",
)
parser.add_argument(
    "-o",
    "--open-result",
    dest="open_result",
    default=False,
    help="Show result picture once it generated",
    action="store_true",
)
parser.add_argument(
    "-w",
    "--warmup-time",
    dest="warmup_time",
    type=int,
    default=0,
    help="Wait before starting Selenium once it's driver is ready (seconds)",
)
parser.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    default=False,
    help="Add some debug texts",
    action="store_true",
)
parser.add_argument(
    "-b",
    "--browser",
    dest="browser",
    default="chrome",
    help="Browser used by Selenium to run screenshot",
)
args = parser.parse_args()

## RUNNER
## TO REFACTOR :kekw:
# Prepare to-compare files
session = get_random_name()
compare = [
    generate_screenshot(
        website=args.source_url, name=f"s-{session}", driver=args.browser
    ),
    generate_screenshot(
        website=args.target_url, name=f"t-{session}", driver=args.browser
    ),
]

# Sort file instances
img_source = Image.open(f"{compare[0]}")
img_comparison = Image.open(f"{compare[1]}")

output_file = f"r-{session}.png"

# The magic
diff = pixel_diffs(img_source, img_comparison)
diff.save(output_file)

if args.open_result:
    Image.open(output_file).show()

if not args.keep_files:
    for fi in compare:
        os.remove(fi)
    os.remove(output_file)
