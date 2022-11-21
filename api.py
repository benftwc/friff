import os
from fastapi import FastAPI
from fastapi.responses import Response, FileResponse
from PIL import Image

from lib.helpers import get_random_name
from lib.screenshot import generate_screenshot, pixel_diffs

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "AAA"}


@app.get("/random-name")
def get_random_name_query(length: int = 14):
    return get_random_name(length)


@app.get(
    "/screenshot",
    response_class=FileResponse,
)
def get_screenshot(source_url: str, target_url: str, browser: str = "chrome"):
    session = get_random_name()
    compare = [
        generate_screenshot(website=source_url, name=f"s-{session}", driver=browser),
        generate_screenshot(website=target_url, name=f"t-{session}", driver=browser),
    ]

    # Sort file instances
    img_source = Image.open(f"{compare[0]}")
    img_comparison = Image.open(f"{compare[1]}")

    output_file = f"r-{session}.png"

    # The magic
    diff = pixel_diffs(img_source, img_comparison)
    diff.save(output_file)

    for fi in compare:
        os.remove(fi)

    return output_file
