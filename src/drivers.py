from selenium import webdriver

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
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = Options()
        options.headless = True

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager("107.0.5304.62").install()),
            options=options,
        )

    if driver_name == "firefox":
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager

        options = Options()
        options.headless = True

        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()), options=options
        )

    if driver is None:
        raise WebdriverVehicleError(f"Vehicle {driver} does not exists yet.")

    driver.set_window_position(0, 0)

    return driver
