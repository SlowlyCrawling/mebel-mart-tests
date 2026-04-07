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
    
    # Ищем все ссылки на странице
    links = driver.find_elements(By.TAG_NAME, "a")
    print("Все ссылки на странице:")
    for i, link in enumerate(links[:30]):
        href = link.get_attribute("href")
        text = link.text[:50] if link.text else ""
        print(f"{i+1}. href={href}")
        print(f"   text={text}")
    
    # Ищем ссылки внутри .product-card
    print("\n\nСсылки внутри .product-card:")
    products = driver.find_elements(By.CSS_SELECTOR, ".product-card")
    for i, product in enumerate(products[:3]):
        print(f"\nТовар {i+1}:")
        links_in_product = product.find_elements(By.TAG_NAME, "a")
        for link in links_in_product:
            href = link.get_attribute("href")
            text = link.text[:50] if link.text else ""
            print(f"  href={href}")
            print(f"  text={text}")
    
    time.sleep(5)
    
finally:
    driver.quit()