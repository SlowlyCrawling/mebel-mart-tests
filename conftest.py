"""
Фикстуры pytest - простая рабочая версия
"""

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура создает и закрывает браузер"""
    print("\n🚀 Запускаю браузер...")
    
    # Создаем папку для скриншотов
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    # Простые настройки (как в работающем тесте)
    options = Options()
    options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    
    print("🔚 Закрываю браузер...")
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL"""
    return "https://mebelmart-saratov.ru"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для скриншотов"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"fail_{item.name}_{timestamp}.png"
                screenshot_path = os.path.join("screenshots", screenshot_name)
                driver.save_screenshot(screenshot_path)
                print(f"\n📸 Скриншот: {screenshot_path}")
            except Exception as e:
                print(f"\n⚠️ Ошибка скриншота: {e}")