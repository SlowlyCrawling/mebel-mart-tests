import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config

@pytest.fixture(scope="function")
def driver():
    if not os.path.exists(Config.SCREENSHOTS_DIR):
        os.makedirs(Config.SCREENSHOTS_DIR)
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return Config.BASE_URL

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join(Config.SCREENSHOTS_DIR, f"fail_{item.name}_{timestamp}.png")
            driver.save_screenshot(path)
            print(f"\n📸 Скриншот: {path}")