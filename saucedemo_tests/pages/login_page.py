# pages/login_page.py
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        time.sleep(1)  # дать странице загрузиться
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(1)

        class LoginPage(BasePage):
            USERNAME_INPUT = (By.ID, "user-name")
            PASSWORD_INPUT = (By.ID, "password")
            LOGIN_BUTTON = (By.ID, "login-button")

            def login(self, username, password):
                self.logger.info(f"Logging in with username: {username}")
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
                self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
                self.driver.find_element(*self.LOGIN_BUTTON).click()
                self.logger.info("Login button clicked")