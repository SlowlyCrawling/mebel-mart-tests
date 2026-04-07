"""
Утилиты для работы со скриншотами
"""

import os
import allure
from datetime import datetime


class ScreenshotUtils:
    
    @staticmethod
    def take_screenshot(driver, name="screenshot", screenshots_dir="screenshots"):
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename)
        
        driver.save_screenshot(filepath)
        return filepath
    
    @staticmethod
    def attach_to_allure(driver, name="Скриншот"):
        screenshot = driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )