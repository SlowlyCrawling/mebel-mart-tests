"""
Простой тест для проверки открытия сайта
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("🚀 Запускаем тест открытия сайта...")

# Запускаем браузер
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    url = "https://mebelmart-saratov.ru/myagkaya_mebel_v_saratove/divanyi_v_saratove"
    print(f"📡 Открываю: {url}")
    
    driver.get(url)
    time.sleep(3)
    
    print(f"✅ Страница открыта!")
    print(f"📄 Заголовок: {driver.title}")
    
    # Делаем скриншот
    driver.save_screenshot("site_opened.png")
    print("📸 Скриншот сохранен: site_opened.png")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
finally:
    driver.quit()
    print("🏁 Браузер закрыт")