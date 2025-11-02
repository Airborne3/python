from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    FINISH_BUTTON = (By.XPATH, "//a[text()='Finish']")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def get_item_names(self):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]

    def get_total_price(self):
        total = self.wait.until(EC.visibility_of_element_located(self.TOTAL_LABEL))
        return total.text  # e.g., "Total: $32.39"

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()