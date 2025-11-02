from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_item_names_in_cart(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        names = [item.find_element(*self.ITEM_NAME).text for item in items]
        self.logger.info(f"Items in cart: {names}")
        return names

    def click_remove_button(self):
        self.logger.info("Clicking 'Remove' button")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON)).click()
        self.logger.info("Item removed from cart")

    def is_cart_empty(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        is_empty = len(items) == 0
        self.logger.info(f"Cart is empty: {is_empty}")
        return is_empty

    def click_continue_shopping(self):
        self.logger.info("Clicking 'Continue Shopping'")
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
        self.logger.info("Returned to inventory page")

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='CHECKOUT']")

    def get_item_names_in_cart(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.find_element(*self.ITEM_NAME).text for item in items]

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()