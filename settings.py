import inspect

webdriver_width_max = 4096
webdriver_width_min = 0
webdriver_width_default = 1920

webdriver_height_max = 4096
webdriver_height_min = 0
webdriver_height_default = 1080

webdriver_default_driver = "chrome"
webdriver_default_warmup_time = 0

screenshots_output_folder = "./renders/"


class WebdriverSizeError(Exception):
    def __init__(self):
        Exception.__init__(self)


class WebdriverVehicleError(Exception):
    def __init__(self):
        Exception.__init__(self)


class ImageComparisonException(Exception):
    def __init__(self):
        Exception.__init__(self)


def Debug(f):
    def wrapper(*args, **kwargs):
        bound_args = inspect.signature(f).bind(*args, **kwargs)
        bound_args.apply_defaults()
        print(f"Method `{f.__name__}` -> ")
        print(dict(bound_args.arguments))
        result = f
        print(result)

        return f(*args, **kwargs)

    return wrapper
