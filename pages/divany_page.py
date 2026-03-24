"""
Page Object для страницы диванов - с правильными селекторами
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DivanyPage(BasePage):
    """Страница диванов"""
    
    # Правильные CSS селекторы на основе анализа
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    PRODUCT_LINKS = (By.CSS_SELECTOR, "a[href*='/product/']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-card__now_price")
    PRODUCT_OLD_PRICE = (By.CSS_SELECTOR, ".product-card__old_price")
    
    # Пагинация
    NEXT_PAGE = (By.CSS_SELECTOR, ".owl-next")
    PREV_PAGE = (By.CSS_SELECTOR, ".owl-prev")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url_path = "/myagkaya_mebel_v_saratove/divanyi_v_saratove"
    
    @allure.step("Открыть страницу диванов")
    def open_page(self, base_url):
        full_url = f"{base_url}{self.url_path}"
        self.open(full_url)
    
    @allure.step("Получить все ссылки на товары")
    def get_product_links(self):
        """Возвращает список ссылок на товары"""
        return self.find_elements(self.PRODUCT_LINKS)
    
    @allure.step("Получить все цены")
    def get_prices(self):
        """Возвращает список цен"""
        return self.find_elements(self.PRODUCT_PRICE)
    
    @allure.step("Кликнуть на первый товар")
    def click_first_product(self):
        """Кликает на первый товар"""
        links = self.get_product_links()
        if links:
            links[0].click()
            return True
        return False
    
    @allure.step("Перейти на следующую страницу")
    def go_to_next_page(self):
        """Кликает на стрелку 'далее'"""
        try:
            next_btn = self.wait.until(EC.element_to_be_clickable(self.NEXT_PAGE))
            next_btn.click()
            return True
        except:
            return False