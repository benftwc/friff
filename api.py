from fastapi import FastAPI
from fastapi.responses import FileResponse

from src.helpers import get_random_name
from src.main import Run

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
def get_screenshot(
    source_url: str, target_url: str, browser: str = "chrome", warmup_time: int = 0
):
    return Run(
        source_url=source_url,
        target_url=target_url,
        browser=browser,
        keep_files=False,
        open_result=False,
        warmup_time=warmup_time,
    )
