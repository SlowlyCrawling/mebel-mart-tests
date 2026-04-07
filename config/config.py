import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Config:
    BASE_URL = "https://mebelmart-saratov.ru"
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    SCREENSHOTS_DIR = "screenshots"
    BROWSERS = ["chrome", "firefox"]

    @staticmethod
    def get_chrome_options():
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return options

    @staticmethod
    def get_firefox_options():
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        return options