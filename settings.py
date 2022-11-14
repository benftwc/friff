#!python
webdriver_width_max=4096
webdriver_width_min=0
webdriver_width_default=1920

webdriver_height_max=4096
webdriver_height_min=0
webdriver_height_default=0

class WebdriverSizeError(Exception):
    def __init__(self):
        Exception.__init__(self)
        
class WebdriverVehicleError(Exception):
    def __init__(self):
        Exception.__init__(self) 
        
class ImageComparisonException(Exception):
    def __init__(self):
        Exception.__init__(self)