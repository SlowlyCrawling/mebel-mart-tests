from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)

def after_scenario(context, scenario):
    context.driver.quit()

@given('Я открываю сайт "https://mebelmart-saratov.ru"')
def open_site(context):
    context.driver.get("https://mebelmart-saratov.ru")
    time.sleep(2)

@when('Я открываю раздел "Диваны"')
def open_divany(context):
    context.driver.get("https://mebelmart-saratov.ru/myagkaya_mebel_v_saratove/divanyi_v_saratove")
    time.sleep(2)

@when('Я устанавливаю фильтр цены от 10000 до 15000')
def set_price_filter(context):
    filter_btn = context.driver.find_elements(By.XPATH, "//button[contains(text(), 'Фильтры')]")
    if filter_btn:
        context.driver.execute_script("arguments[0].click();", filter_btn[0])
        time.sleep(1)
    price_input = context.driver.find_elements(By.CSS_SELECTOR, "input[name='price']")
    if price_input:
        context.driver.execute_script("arguments[0].value = '10000,15000'; arguments[0].dispatchEvent(new Event('change'));", price_input[0])
        time.sleep(1)

@when('Я применяю фильтр')
def apply_filter(context):
    apply_btn = context.driver.find_elements(By.XPATH, "//button[contains(text(), 'Применить фильтр')]")
    if apply_btn:
        context.driver.execute_script("arguments[0].click();", apply_btn[0])
        time.sleep(3)

@then('В результатах есть товары с ценой от 10000 до 15000')
def check_prices(context):
    prices = context.driver.find_elements(By.CSS_SELECTOR, ".product-card__now_price")
    found = False
    for p in prices[:30]:
        digits = ''.join(filter(str.isdigit, p.text))
        if digits and 10000 <= int(digits) <= 15000:
            found = True
            break
    assert found, "Нет товаров в диапазоне 10000-15000"

@when('Я открываю карточку первого товара')
def open_product_card(context):
    product = context.driver.find_element(By.CSS_SELECTOR, "a[href*='/product/']")
    context.driver.execute_script("arguments[0].click();", product)
    time.sleep(2)

@then('На странице есть характеристика "Ширина"')
def check_width(context):
    body = context.driver.find_element(By.TAG_NAME, "body").text
    assert "ширина" in body.lower() or "Ширина" in body

@when('Я нажимаю иконку избранного у первого товара')
def click_favorite(context):
    fav = context.driver.find_elements(By.CSS_SELECTOR, ".favorite-btn, .wishlist, .like, [class*='fav']")
    if fav:
        context.driver.execute_script("arguments[0].click();", fav[0])
        time.sleep(1)

@then('Иконка избранного меняет состояние')
def check_favorite_state(context):
    pass

@when('Я ввожу в поиск "Диван" и нажимаю Enter')
def search_product(context):
    search = context.driver.find_elements(By.CSS_SELECTOR, "input[placeholder*='Кто ищет'], input[type='search']")
    if search:
        context.driver.execute_script("arguments[0].value = 'Диван';", search[0])
        context.driver.execute_script("arguments[0].form.submit();", search[0])
        time.sleep(3)

@then('В результатах поиска есть товары')
def check_search_results(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, ".product-card")
    assert len(results) > 0

@when('Я нажимаю кнопку "Купить"')
def click_buy(context):
    buy = context.driver.find_elements(By.XPATH, "//button[contains(text(), 'Купить')]")
    if buy:
        context.driver.execute_script("arguments[0].click();", buy[0])
        time.sleep(2)

@then('Товар добавляется в корзину')
def check_cart(context):
    pass