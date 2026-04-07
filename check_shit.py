from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
try:
    driver.get("https://mebelmart-saratov.ru/myagkaya_mebel_v_saratove/divanyi_v_saratove")
    time.sleep(3)
    print(f"Страница открыта. Заголовок: {driver.title}")
    driver.save_screenshot("test_open.png")
    print("Скриншот сохранён")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    driver.quit()