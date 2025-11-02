from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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