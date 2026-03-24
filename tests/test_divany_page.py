"""
Реальные тесты для страницы диванов
"""

import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.divany_page import DivanyPage


@allure.feature("Страница диванов")
class TestDivanyPageReal:
    """Реальные тесты"""
    
    def close_cookie_banner(self, driver):
        """Закрывает куки-баннер если есть"""
        try:
            # Ищем кнопку закрытия куки
            close_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Принять')]")
            for btn in close_buttons:
                if btn.is_displayed():
                    btn.click()
                    time.sleep(0.5)
                    print("🍪 Куки закрыты")
                    break
        except:
            pass
    
    def scroll_to_element(self, driver, element):
        """Прокручивает к элементу"""
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
    
    @allure.title("Тест 1: Проверка количества товаров на странице")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_products_count(self, driver, base_url):
        """Проверяет что на странице есть товары"""
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(3)
        
        # Закрываем куки
        self.close_cookie_banner(driver)
        
        # Ищем товары по ссылкам на продукт
        products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/product/']")
        print(f"📦 Найдено товаров: {len(products)}")
        
        # Убираем дубликаты
        unique_products = list(set([p.get_attribute("href") for p in products]))
        print(f"📦 Уникальных товаров: {len(unique_products)}")
        
        assert len(unique_products) > 0, "На странице нет товаров!"
        
        page._take_screenshot("products_count")
        print("✅ Тест пройден")
    
    @allure.title("Тест 2: Проверка цен товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_prices_exist(self, driver, base_url):
        """Проверяет что у товаров есть цены"""
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(3)
        
        # Закрываем куки
        self.close_cookie_banner(driver)
        
        # Ищем цены
        prices = driver.find_elements(By.CSS_SELECTOR, ".product-card__now_price")
        
        if not prices:
            prices = driver.find_elements(By.CSS_SELECTOR, "[class*='price']")
        
        print(f"💰 Найдено цен: {len(prices)}")
        
        # Выводим первые 5 цен
        valid_prices = 0
        for i, price in enumerate(prices[:10]):
            price_text = price.text.strip()
            if price_text and "₽" in price_text:
                valid_prices += 1
                print(f"  Цена {i+1}: {price_text}")
        
        assert valid_prices > 0, "Нет валидных цен!"
        
        page._take_screenshot("prices")
        print("✅ Тест пройден")
    
    @allure.title("Тест 3: Клик по первому товару")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_first_product(self, driver, base_url):
        """Кликает на первый товар и проверяет переход"""
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(3)
        
        # Закрываем куки
        self.close_cookie_banner(driver)
        
        # Находим ссылки на товары
        products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/product/']")
        
        # Фильтруем уникальные ссылки
        seen = set()
        unique_links = []
        for p in products:
            href = p.get_attribute("href")
            if href and href not in seen and "product" in href:
                seen.add(href)
                unique_links.append(p)
        
        print(f"🔗 Найдено уникальных ссылок: {len(unique_links)}")
        
        if len(unique_links) > 0:
            first_product = unique_links[0]
            
            # Прокручиваем к элементу
            self.scroll_to_element(driver, first_product)
            time.sleep(1)
            
            # Получаем URL до клика
            url_before = driver.current_url
            
            # Пробуем кликнуть через JavaScript
            driver.execute_script("arguments[0].click();", first_product)
            time.sleep(3)
            
            # Проверяем что URL изменился
            url_after = driver.current_url
            print(f"🔗 URL до: {url_before}")
            print(f"🔗 URL после: {url_after}")
            
            assert url_after != url_before, "URL не изменился после клика"
            assert "/product/" in url_after, "Не открылась страница товара"
            
            page._take_screenshot("product_opened")
            print(f"✅ Открыт товар")
        else:
            pytest.fail("Не найдено ссылок на товары")
    
    @allure.title("Тест 4: Проверка наличия навигации")
    @allure.severity(allure.severity_level.NORMAL)
    def test_navigation_exists(self, driver, base_url):
        """Проверяет наличие элементов навигации"""
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(3)
        
        # Закрываем куки
        self.close_cookie_banner(driver)
        
        # Ищем кнопки навигации
        nav_buttons = driver.find_elements(By.CSS_SELECTOR, ".owl-prev, .owl-next, .pagination a")
        
        print(f"🔍 Найдено кнопок навигации: {len(nav_buttons)}")
        
        for btn in nav_buttons:
            print(f"  Кнопка: {btn.get_attribute('class')} -> текст: {btn.text}")
        
        # Проверяем что есть хотя бы одна кнопка навигации
        assert len(nav_buttons) > 0, "Нет кнопок навигации!"
        
        page._take_screenshot("navigation")
        print("✅ Тест пройден")
    
    @allure.title("Тест 5: Проверка названий товаров")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_names(self, driver, base_url):
        """Проверяет что у товаров есть названия"""
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(3)
        
        # Закрываем куки
        self.close_cookie_banner(driver)
        
        # Ищем названия товаров
        names = driver.find_elements(By.CSS_SELECTOR, ".product-card__title, .product-name, [class*='title']")
        
        # Фильтруем пустые
        valid_names = [n.text.strip() for n in names if n.text.strip()]
        
        print(f"📝 Найдено названий: {len(valid_names)}")
        
        for name in valid_names[:5]:
            print(f"  Название: {name[:50]}")
        
        assert len(valid_names) > 0, "Нет названий товаров"
        
        page._take_screenshot("names")
        print("✅ Тест пройден")
    
    @allure.title("Тест 6: Проверка наличия изображений")
    @allure.severity(allure.severity_level.MINOR)
    def test_images_exist(self, driver, base_url):
        """Проверяет что на странице есть изображения товаров"""
        page = DivanyPage(driver)
        page.open_page(base_url)
        time.sleep(3)
        
        # Закрываем куки
        self.close_cookie_banner(driver)
        
        # Ищем изображения
        images = driver.find_elements(By.CSS_SELECTOR, "img")
        
        # Фильтруем иконки и маленькие картинки
        valid_images = []
        for img in images:
            src = img.get_attribute("src")
            if src and "icon" not in src and "logo" not in src and "svg" not in src:
                width = img.get_attribute("width")
                if width and width.isdigit() and int(width) > 50:
                    valid_images.append(img)
                elif not width:
                    valid_images.append(img)
        
        print(f"🖼️ Найдено изображений: {len(images)}")
        print(f"🖼️ Валидных изображений: {len(valid_images)}")
        
        # Проверяем что есть хотя бы 3 изображения
        assert len(valid_images) > 3, f"Слишком мало изображений: {len(valid_images)}"
        
        page._take_screenshot("images")
        print("✅ Тест пройден")