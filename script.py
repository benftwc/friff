# Imports
import argparse
import random
import string

from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import settings as SETTINGS

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
    action='store_true',
)
parser.add_argument(
    "-p",
    "--purge-files",
    dest="purge_files",
    default=False,
    help="Remove files before take screenshots",
    action='store_true',
)
parser.add_argument(
    "-o",
    "--open-result",
    dest="open_result",
    default=False,
    help="Show result picture once it generated",
    action='store_true',
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
    action='store_true',
)
args = parser.parse_args()

# Lib internals
def trace_debug(message, enabled=args.verbose):
    """Trace logs/message once verbose mode is enabled

    Args:
        message (string): Message to display
        enabled (boolean, optional): Enable verbose mode. Defaults to True.
    """
    if enabled:
        print(message)
    
trace_debug(args)

def pixel_diffs(source, comparison):
    """Do the magic.

    Check wether images are same and produce image based on two derivates.

    If no differences between SOURCE and TARGET, then result image will be black

    Args:
        source (Image): The Source image to compare with
        comparison (Image): The Target/Comparison image

    Raises:
        Exception: _description_
        Exception: _description_

    Returns:
        Image: Render of source MINUS target (black output if no diff)
    """
    if source.size != comparison.size:
        raise SETTINGS.ImageComparisonException("Different image sizes")

    if source.mode != comparison.mode:
        raise SETTINGS.ImageComparisonException("Different picture mods")

    diff = ImageChops.difference(source, comparison)

    return diff.convert("L")

def get_random_name(size=10):
    """Generate random string

    Args:
        size (int, optional): String length. Defaults to 10.

    Returns:
        string: Random string
    """
    return ''.join(random.choice(string.ascii_lowercase) for i in range(size))

def get_driver(driver_name="chrome"):
    """Prepare Webdriver to be used

    Returns:
        WebDriver: WebDriver instance warmed up
    """
    options = Options()
    options.headless = True

    driver_name = driver_name.lower()
    driver = None
    
    if driver_name == "chrome":
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
    
    if driver_name == "firefox":
        driver = webdriver.Firefox(
            service=Service(ChromeDriverManager().install()), options=options
        )
    
    if driver is None:
        raise SETTINGS.WebdriverVehicleError(f"Vehicle {driver} does not exists yet.")
    
    driver.set_window_position(0, 0)
    
    return driver
    
def generate_screenshot(website, name, width=SETTINGS.webdriver_width_default, height=SETTINGS.webdriver_height_default):
    """Based on its URL, generate Website screenshot

    Args:
        website (str): Website to screenshot
        type (str, optional): Output filename. Defaults to 'source'.
        width (int, optional): The webdriver width. Defaults to SETTINGS.webdriver_width_default (1920).
        height (int, optional): The webdriver height. Defaults to SETTINGS.webdriver_height_default (1080).

    Raises:
        SETTINGS.WebdriverSizeError: Size does not respect min/max values

    Returns:
        str: The saved screenshot path
    """
    if int(width) < SETTINGS.webdriver_width_min or int(width) > SETTINGS.webdriver_width_max:
        raise SETTINGS.WebdriverSizeError()
    
    driver = get_driver()
    driver.get(website)
    driver.set_window_size(width, height)
    screenshot_name = f"{name}.png"
    driver.save_screenshot(screenshot_name)
    driver.quit()

    return screenshot_name


## RUNNER
## TO REFACTOR :kekw:
# Prepare to-compare files
session = get_random_name()
compare = [
    generate_screenshot(website=args.source_url, name=f"s-{session}"),
    generate_screenshot(website=args.target_url, name=f"t-{session}"),
]

# Sort file instances
img_source = Image.open(f"{compare[0]}")
img_comparison = Image.open(f"{compare[1]}")

output_file = "diff-output.png"

# The magic
diff = pixel_diffs(img_source, img_comparison)
diff.save(output_file)

if args.open_result:
    Image.open(output_file).show()
