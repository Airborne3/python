# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.logger import get_logger

logger = get_logger("conftest")


@pytest.fixture(scope="function")
def driver():
    logger.info("Starting WebDriver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Явно открываем логин-страницу
    driver.get("https://www.saucedemo.com/")

    # Очищаем куки и localStorage на всякий случай
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")

    # Перезагружаем страницу, чтобы убедиться, что мы на логине
    driver.get("https://www.saucedemo.com/")

    logger.info("Opened SauceDemo login page")
    yield driver
    driver.quit()
    logger.info("WebDriver closed")

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # chrome_options.add_argument("--headless")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
