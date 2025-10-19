import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_as_admin(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.click()
    username_input.send_keys("Admin")
    password_input.click()
    password_input.send_keys("admin123")

    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()

    time.sleep(3)
    assert "dashboard" in driver.current_url, "Не удалось войти в систему"

    admin_link = driver.find_element(By.LINK_TEXT, "Admin") # <a href="https://">Admin</a>
    assert admin_link.is_displayed(), "Ссылка Admin не отображается на странице или не найдена"

    admin_link.click()
    time.sleep(1)
    driver.save_screenshot("screen_admin_page.png")
    time.sleep(3)