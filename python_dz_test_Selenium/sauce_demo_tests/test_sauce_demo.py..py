import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument()
    options.add_argument("--no-default-browser-check")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_standard_user_checkout_flow(driver):
    # 1. Вход в систему
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    assert "inventory.html" in driver.current_url

    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()

    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    assert "cart.html" in driver.current_url

    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert cart_item.text == "Sauce Labs Backpack"

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    assert "checkout-step-one.html" in driver.current_url
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()


    assert "checkout-step-two.html" in driver.current_url


    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()


    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert success_message.text == "Thank you for your order!"