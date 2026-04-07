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
    
  
    filter_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Фильтры')]")
    if filter_btn:
        filter_btn[0].click()
        time.sleep(1)
        print("'Фильтры' нажата")
    
    print("\n'Цена'")
    price_labels = driver.find_elements(By.XPATH, "//*[contains(text(), 'Цена')]")
    for el in price_labels:
        print(f"Текст: {el.text}, Тег: {el.tag_name}, Class: {el.get_attribute('class')}")
    
    print("\nВсе input элементы")
    inputs = driver.find_elements(By.TAG_NAME, "input")
    for inp in inputs:
        print(f"Type: {inp.get_attribute('type')}, Class: {inp.get_attribute('class')}, Placeholder: {inp.get_attribute('placeholder')}")
    
    print("\nВсе range ползунки")
    ranges = driver.find_elements(By.CSS_SELECTOR, "input[type='range']")
    print(f"Найдено range: {len(ranges)}")
    for r in ranges:
        print(f"  min={r.get_attribute('min')}, max={r.get_attribute('max')}, value={r.get_attribute('value')}")
    
    print("\nКнопка 'Применить фильтр'")
    apply = driver.find_elements(By.XPATH, "//button[contains(text(), 'Применить фильтр')]")
    print(f"Найдено: {len(apply)}")
    
    time.sleep(5)
    
finally:
    driver.quit()

    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    import time
    import traceback

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://mebelmart-saratov.ru/myagkaya_mebel_v_saratove/divanyi_v_saratove")
        time.sleep(3)
        
        filter_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Фильтры')]")
        if filter_btn:
            driver.execute_script("arguments[0].click();", filter_btn[0])
            print("✅ Кнопка 'Фильтры' нажата")
            time.sleep(2)
        
        print("\nВСЕ ЭЛЕМЕНТЫ")
        
        ranges = driver.find_elements(By.CSS_SELECTOR, "input[type='range']")
        print(f"1. Найдено (range): {len(ranges)}")
        for r in ranges:
            print(f"   → min={r.get_attribute('min')}, max={r.get_attribute('max')}, value={r.get_attribute('value')}")
        
      
        number_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='number'], input[type='text']")
        print(f"\n2. Наайдено полей ввода: {len(number_inputs)}")
        for inp in number_inputs[:10]:
            print(f"   → placeholder={inp.get_attribute('placeholder')}, value={inp.get_attribute('value')}")
        
        min_max = driver.find_elements(By.CSS_SELECTOR, "[min][max]")
        print(f"\n3. Найдено элементов с min/max: {len(min_max)}")
        for el in min_max[:10]:
            print(f"   → tag={el.tag_name}, min={el.get_attribute('min')}, max={el.get_attribute('max')}")
        
        driver.save_screenshot("after_manual_open.png")
        print("\n after_manual_open.png")
        
        time.sleep(5)
        
    finally:
        driver.quit()