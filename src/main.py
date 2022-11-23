import os

from PIL import Image

import settings as SETTINGS
from src.helpers import get_random_name, init_render_folder
from src.screenshot import generate_screenshot, pixel_diffs

def Run(
    source_url: str,
    target_url: str,
    browser: str = "chrome",
    open_result: bool = False,
    keep_files: bool = False,
    warmup_time: int = 0,
    screenshot_extension:str = SETTINGS.screenshots_output_extension
):
    """Main runner as different systems may start Bot

    Args:
        source_url (str): Source URL
        target_url (str): Target URL
        browser (str, optional): Browser used by Runner. Defaults to "chrome".
        open_result (bool, optional): Display results (CLI). Defaults to False.
        keep_files (bool, optional): Keeps temporary files. Defaults to False.

    Returns:
        string: URI to generated picture
    """
    # Prepare the render folder
    init_render_folder(SETTINGS.screenshots_output_folder)

    # Comparison session name generation
    # Used to store/load/cache Comparison queries
    session = get_random_name(32)
    compare = [
        generate_screenshot(
            website=source_url,
            name=f"s-{session}",
            driver=browser,
            warmup_time=warmup_time,
            extension=screenshot_extension
        ),
        generate_screenshot(
            website=target_url,
            name=f"t-{session}",
            driver=browser,
            warmup_time=warmup_time,
            extension=screenshot_extension
        ),
    ]

    # Sort file instances
    img_source = Image.open(f"{compare[0]}")
    img_comparison = Image.open(f"{compare[1]}")

    # Prepare the output
    output_file = f"{SETTINGS.screenshots_output_folder}r-{session}.{screenshot_extension}"

    # The magic
    diff = pixel_diffs(img_source, img_comparison)
    diff.save(output_file)

    if open_result:
        Image.open(output_file).show()
    else:
        return output_file

    if not keep_files:
        for fi in compare:
            os.remove(fi)
        os.remove(output_file)
