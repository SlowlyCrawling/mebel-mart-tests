# tests/test_simple.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_simple():
    """Простейший тест без фикстур"""
    print("\n🚀 Запускаю браузер...")
    
    options = Options()
    options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://mebelmart-saratov.ru")
        print(f"✅ Заголовок: {driver.title}")
        assert "мебель" in driver.title.lower()
    finally:
        driver.quit()
        print("🔚 Браузер закрыт")