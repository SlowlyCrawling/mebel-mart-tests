# run_tests.py - запуск тестов без pytest
import sys
import os

# Добавляем путь к проекту
sys.path.insert(0, os.path.dirname(__file__))

from pages.divany_page import DivanyPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def run_test():
    print("="*50)
    print("🚀 ЗАПУСК ТЕСТА (без pytest)")
    print("="*50)
    
    # Настройки как в работающем тесте
    options = Options()
    options.add_argument("--start-maximized")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        page = DivanyPage(driver)
        page.open_page("https://mebelmart-saratov.ru")
        
        time.sleep(3)
        
        title = page.get_title()
        print(f"📄 Заголовок: {title}")
        
        products_count = page.get_products_count()
        print(f"📦 Товаров: {products_count}")
        
        print("\n✅ ТЕСТ ПРОШЕЛ!")
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {e}")
        
    finally:
        driver.quit()
        print("🔚 Браузер закрыт")

if __name__ == "__main__":
    run_test()