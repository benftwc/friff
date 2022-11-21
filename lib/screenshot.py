from PIL import ImageChops

import settings as SETTINGS
from lib.drivers import get_driver
from settings import Debug


@Debug
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


@Debug
def generate_screenshot(
    website,
    name,
    width=SETTINGS.webdriver_width_default,
    height=SETTINGS.webdriver_height_default,
    driver=SETTINGS.webdriver_default_driver,
):
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
    if (
        int(width) < SETTINGS.webdriver_width_min
        or int(width) > SETTINGS.webdriver_width_max
    ):
        raise SETTINGS.WebdriverSizeError()

    if (
        int(height) < SETTINGS.webdriver_height_min
        or int(height) > SETTINGS.webdriver_height_max
    ):
        raise SETTINGS.WebdriverSizeError()

    driver = get_driver(driver)
    driver.get(website)
    driver.set_window_size(width, height)
    screenshot_name = f"{name}.png"
    driver.save_screenshot(screenshot_name)
    driver.quit()

    return screenshot_name
