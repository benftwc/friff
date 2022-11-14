# Imports
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import argparse

# Prepare Arguments Parser
parser = argparse.ArgumentParser(description="Take screenshot and compare them to get differences between two given environments")
parser.add_argument('-s', '--source', metavar='URL',dest='source_url', type=str, help="The source website URL")
parser.add_argument('-t', '--target', metavar='URL',dest='target_url', type=str, help="The target website URL")
parser.add_argument('-k', '--keep-files', dest='keep_files', type=bool, default=True, help="True to keep files after comparison")
parser.add_argument('-p', '--purge-files', dest='purge_files', type=bool,default=True, help='True to remove files before take screenshots')
parser.add_argument('-o', '--open-result', dest='open_result', type=bool, default=False, help='Show result picture once it generated')
args = parser.parse_args()

print(args)

# Lib internals
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
        raise Exception("Different image sizes")

    if source.mode != comparison.mode:
        raise Exception("Different picture mods")

    diff = ImageChops.difference(source, comparison)

    return diff.convert('L')

def generate_screenshot(website, type='source', extension='png'):
    """Based on its URL, generate Website screenshot

    Args:
        website (str): Website to screenshot
        type (str, optional): Output filename. Defaults to 'source'.
        extension (str, optional): Output file extension. Defaults to 'png'.

    Returns:
        str: The saved screenshot path
    """
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_position(0,0)
    driver.set_window_size(1920,1080)
    driver.get(website)

    screenshot_name = f"{type}.{extension}"
    driver.save_screenshot(screenshot_name)
    driver.quit()

    return screenshot_name



## RUNNER
# Prepare to-compare files
compare = [generate_screenshot(args.source_url, "source"), generate_screenshot(args.target_url, "target")]

# Sort file instances
img_source = Image.open(f"{compare[0]}")
img_comparison = Image.open(f"{compare[1]}")

output_file = "diff-output.png"

# The magic
diff = pixel_diffs(img_source, img_comparison)
diff.save(output_file)

if args.open_result:
    Image.open(output_file).show()
