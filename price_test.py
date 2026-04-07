@allure.title("2.1 Фильтрация по цене от 10000 до 15000")
def test_filter_by_price(self, driver, base_url):
    page = DivanyPage(driver)
    page.open_page(base_url)
    time.sleep(2)
    self.close_cookie(driver)

    # 1. Открываем фильтры
    filter_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Фильтры')]")
    if filter_btn:
        driver.execute_script("arguments[0].click();", filter_btn[0])
        time.sleep(1)

    # 2. Находим скрытое поле цены и устанавливаем диапазон
    price_input = driver.find_elements(By.CSS_SELECTOR, "input[name='price']")
    if price_input:
        driver.execute_script("arguments[0].value = '10000,15000'; arguments[0].dispatchEvent(new Event('change'));", price_input[0])
        time.sleep(1)

    # 3. Применяем фильтр
    apply_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Применить фильтр')]")
    if apply_btn:
        driver.execute_script("arguments[0].click();", apply_btn[0])
        time.sleep(3)

    # 4. Проверяем, что есть товар с ценой от 10000 до 15000
    prices = driver.find_elements(By.CSS_SELECTOR, ".product-card__now_price")
    found = False
    for p in prices[:20]:
        digits = ''.join(filter(str.isdigit, p.text))
        if digits and 10000 <= int(digits) <= 15000:
            found = True
            print(f"✅ Найден товар с ценой: {p.text}")
            break

    assert found, "Нет товаров в диапазоне 10000-15000"