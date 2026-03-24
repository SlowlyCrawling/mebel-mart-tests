"""
Базовый класс для всех страниц
"""

import os
import allure
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from config.config import Config


class BasePage:
    """Базовый класс для всех Page Object"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def _take_screenshot(self, name="screenshot"):
        """Делает скриншот даже если тест прошел"""
        try:
            if not os.path.exists(Config.SCREENSHOTS_DIR):
                os.makedirs(Config.SCREENSHOTS_DIR)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(Config.SCREENSHOTS_DIR, filename)
            self.driver.save_screenshot(filepath)
            print(f"📸 Скриншот: {filepath}")
            
            # Прикрепляем к Allure
            with open(filepath, 'rb') as f:
                allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)
            
            return filepath
        except Exception as e:
            print(f"⚠️ Ошибка скриншота: {e}")
            return None
    
    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        """Открывает URL с обработкой ошибок"""
        try:
            print(f"Загружаю: {url}")
            self.driver.get(url)
            self.wait_for_page_load()
        except WebDriverException as e:
            print(f"❌ Ошибка при открытии {url}: {e}")
            self._take_screenshot("error_open")
            raise
    
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        """Находит элемент с явным ожиданием"""
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException as e:
            print(f"❌ Элемент не найден: {locator}")
            self._take_screenshot("element_not_found")
            raise
    
    @allure.step("Найти элементы: {locator}")
    def find_elements(self, locator):
        """Находит все элементы по локатору"""
        try:
            self.wait.until(
                EC.presence_of_element_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []
    
    @allure.step("Кликнуть на элемент: {locator}")
    def click(self, locator):
        """Кликает на элемент"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        """Получает текст элемента"""
        element = self.find_element(locator)
        return element.text
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_element_visible(self, locator):
        """Проверяет виден ли элемент"""
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Ожидать загрузки страницы")
    def wait_for_page_load(self):
        """Ожидает полной загрузки страницы"""
        try:
            self.wait.until(
                lambda driver: driver.execute_script(
                    "return document.readyState"
                ) == "complete"
            )
        except TimeoutException:
            print("⚠️ Таймаут загрузки страницы")
            self._take_screenshot("timeout")
            raise