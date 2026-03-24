"""
Конфигурационный файл
"""

import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class Config:
    """Конфигурация тестов"""
    
    # Базовый URL сайта
    BASE_URL = "https://mebelmart-saratov.ru"
    
    # Таймауты
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Директории
    SCREENSHOTS_DIR = "screenshots"
    
    # Поддерживаемые браузеры
    BROWSERS = ["chrome", "firefox"]
    
    @staticmethod
    def get_chrome_options():
        """Опции для Chrome - минимальная конфигурация"""
        options = ChromeOptions()
        
        # Только самые необходимые опции
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        
        # Отключаем автоматизацию (чтобы сайт не блокировал)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # User-Agent обычного браузера
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        
        return options
    
    @staticmethod
    def get_firefox_options():
        """Опции для Firefox"""
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        return options