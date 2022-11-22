#!/usr/bin/env python3

import argparse

from lib.main import Run

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

Run(
    source_url=args.source_url,
    target_url=args.target_url,
    browser=args.browser,
    keep_files=args.keep_files,
    open_result=args.open_result,
    warmup_time=args.warmup_time,
)
