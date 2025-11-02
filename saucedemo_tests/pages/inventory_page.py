from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def add_first_item_to_cart(self):
        self.logger.info("Adding first item to cart")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()
        self.logger.info("First item added to cart")

    def go_to_cart(self):
        self.logger.info("Navigating to cart page")
        self.driver.find_element(*self.CART_LINK).click()
        self.logger.info("Cart page opened")

    def get_first_item_name(self):
        item_name = self.driver.find_element(*self.ITEM_NAME).text
        self.logger.info(f"First item name: {item_name}")
        return item_name

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='ADD TO CART']")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    FIRST_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def get_first_item_name(self):
        return self.wait.until(EC.presence_of_element_located(self.FIRST_ITEM_NAME)).text

    def add_first_item_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()