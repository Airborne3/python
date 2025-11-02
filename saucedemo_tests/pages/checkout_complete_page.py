from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    COMPLETE_HEADER = (By.XPATH, "//h2[@class='complete-header']")
    BACK_HOME_BUTTON = (By.XPATH, "//button[text()='Back Home']")

    def get_complete_header_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER)).text

    def click_back_home(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME_BUTTON)).click()