from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as GeckoOptions
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from settings import Debug, WebdriverVehicleError


@Debug
def get_driver(driver_name="chrome"):
    """Prepare Webdriver to be used

    Returns:
        WebDriver: WebDriver instance warmed up
    """

    driver_name = driver_name.lower()
    driver = None

    if driver_name == "chrome":
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager("107.0.5304.62").install()),
            options=options,
        )

    if driver_name == "firefox":
        options = GeckoOptions()
        options.headless = True

        driver = webdriver.Firefox(
            service=GeckoService(GeckoDriverManager().install()), options=options
        )

    if driver is None:
        raise WebdriverVehicleError(f"Vehicle {driver} does not exists yet.")

    driver.set_window_position(0, 0)

    return driver
