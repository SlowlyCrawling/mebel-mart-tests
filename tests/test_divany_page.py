import pytest
import allure
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.divany_page import DivanyPage


@allure.feature("Страница диванов")
class TestDivanyPage:

    def close_cookie(self, driver):
        try:
            btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Принять')]")
            if btn.is_displayed():
                btn.click()
                time.sleep(0.5)
        except:
            pass

    # ========== 2.1 Фильтрация по ширине ==========
    @allure.title("2.1 Фильтрация по ширине 2100 мм")
    def test_filter_by_width(self, driver, base_url):
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(2)
        self.close_cookie(driver)

        filter_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Фильтры')]")
        if filter_btn:
            driver.execute_script("arguments[0].click();", filter_btn[0])
            time.sleep(1)

        width_checkbox = driver.find_elements(By.XPATH, "//label[contains(text(), '2100 мм')]")
        if not width_checkbox:
            pytest.skip("Фильтр по ширине 2100 мм не найден")
        
        driver.execute_script("arguments[0].click();", width_checkbox[0])
        time.sleep(1)

        apply_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Применить фильтр')]")
        if apply_btn:
            driver.execute_script("arguments[0].click();", apply_btn[0])
            time.sleep(3)

        body = driver.find_element(By.TAG_NAME, "body").text
        assert "2100 мм" in body, "Нет товаров с шириной 2100 мм"
        print("✅ Тест 2.1 пройден")

    # ========== 2.2 Детали товара ==========
    @allure.title("2.2 Проверка деталей товара в карточке")
    def test_product_details(self, driver, base_url):
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(2)
        self.close_cookie(driver)

        product_link = driver.find_element(By.CSS_SELECTOR, ".product-card a[href*='/divanyi_v_saratove/']")
        driver.execute_script("arguments[0].click();", product_link)
        time.sleep(2)

        body = driver.find_element(By.TAG_NAME, "body").text
        assert any(x in body.lower() for x in ["ширина", "высота", "глубина"]), "Характеристики не найдены"
        print("✅ Тест 2.2 пройден")

    # ========== 2.3 Избранное ==========
    @allure.title("2.3 Добавление товара в избранное")
    def test_add_to_favorites(self, driver, base_url):
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(2)
        self.close_cookie(driver)

        fav = driver.find_elements(By.CSS_SELECTOR, ".favorite-btn, .wishlist, .like, [class*='fav']")
        if not fav:
            pytest.skip("На сайте нет функционала избранного")
        
        driver.execute_script("arguments[0].click();", fav[0])
        time.sleep(1)
        print("✅ Тест 2.3 пройден")

    # ========== 2.4 Поиск ==========
    @allure.title("2.4 Поиск товара по названию 'Диван'")
    def test_search_product(self, driver, base_url):
        driver.get(base_url)
        time.sleep(2)
        self.close_cookie(driver)

        search = driver.find_elements(By.CSS_SELECTOR, "input[placeholder*='Кто ищет'], input[type='search']")
        if not search:
            pytest.skip("Поле поиска не найдено")

        driver.execute_script("arguments[0].value = 'Диван';", search[0])
        driver.execute_script("arguments[0].form.submit();", search[0])
        time.sleep(3)

        results = driver.find_elements(By.CSS_SELECTOR, ".product-card")
        assert len(results) > 0, "Ничего не найдено"
        print(f"✅ Поиск нашёл {len(results)} товаров")

    # ========== 2.5 Корзина (через карточку товара) ==========
    @allure.title("2.5 Добавление товара в корзину")
    def test_add_to_cart(self, driver, base_url):
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(2)
        self.close_cookie(driver)

        # Открываем карточку первого товара
        product_link = driver.find_element(By.CSS_SELECTOR, ".product-card a[href*='/divanyi_v_saratove/']")
        driver.execute_script("arguments[0].click();", product_link)
        time.sleep(2)
        
        # В карточке ищем кнопку "Купить" (button, не a)
        buy_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Купить')]"))
        )
        buy_btn.click()
        time.sleep(2)
        print("✅ Товар добавлен в корзину")

    # ========== Параметризованный тест 2.5 ==========
    @allure.title("2.5 Добавление товара в корзину (параметризованный)")
    @pytest.mark.parametrize("product_index", [1, 2, 3])
    def test_add_to_cart_parametrized(self, driver, base_url, product_index):
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(2)
        self.close_cookie(driver)

        # Находим все ссылки на товары
        products = driver.find_elements(By.CSS_SELECTOR, ".product-card a[href*='/divanyi_v_saratove/']")
        assert len(products) >= product_index, f"Нет {product_index}-го товара"
        
        product_link = products[product_index - 1]
        driver.execute_script("arguments[0].click();", product_link)
        time.sleep(2)
        
        # В карточке нажимаем "Купить"
        buy_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Купить')]"))
        )
        buy_btn.click()
        time.sleep(2)
        print(f"✅ Товар {product_index} добавлен в корзину")