from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DivanyPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    PRODUCT_LINKS = (By.CSS_SELECTOR, "a[href*='/product/']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-card__now_price")

    def __init__(self, driver):
        super().__init__(driver)
        self.url_path = "/myagkaya_mebel_v_saratove/divanyi_v_saratove"

    def open_page(self, base_url):
        self.open(f"{base_url}{self.url_path}")