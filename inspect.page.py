
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get("https://mebelmart-saratov.ru/myagkaya_mebel_v_saratove/divanyi_v_saratove")
    time.sleep(3)

    print("\n DIV с классами ")
    divs = driver.find_elements(By.TAG_NAME, "div")
    classes = set()
    for div in divs[:50]:
        cls = div.get_attribute("class")
        if cls:
            classes.add(cls)
    
    for c in sorted(classes)[:15]:
        print(f"  {c}")
    
    print("\n КНОПКИ ")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for btn in buttons[:10]:
        print(f"  {btn.text[:50]} -> class: {btn.get_attribute('class')}")
    
    print("\n Ссылки НА ТОВАРЫ")
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='tovar'], a[href*='product']")
    for link in links[:5]:
        print(f"  {link.text[:50]} -> {link.get_attribute('href')}")
    
    print("\n ЦЕНЫ ")
    prices = driver.find_elements(By.CSS_SELECTOR, "[class*='price'], [class*='Price']")
    for price in prices[:5]:
        print(f"  {price.text[:50]} -> class: {price.get_attribute('class')}")
    
    time.sleep(5)
    
finally:
    driver.quit()