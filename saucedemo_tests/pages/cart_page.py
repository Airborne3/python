from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='REMOVE']")

    def get_item_names_in_cart(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.find_element(*self.ITEM_NAME).text for item in items]

    def click_remove_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON)).click()

    def is_cart_empty(self):
        return len(self.driver.find_elements(*self.CART_ITEMS)) == 0