# tests/test_cart_full_flow.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import get_logger

logger = get_logger(__name__)


def test_add_and_remove_item_from_cart(driver):
    logger.info("=== Starting test: test_add_and_remove_item_from_cart ===")

    # Инициализация страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Шаг 1: Логин
    login_page.login("standard_user", "secret_sauce")
    logger.info("User logged in successfully")

    # Шаг 2: Запоминаем название первого товара
    expected_item = inventory_page.get_first_item_name()

    # Шаг 3: Добавляем в корзину
    inventory_page.add_first_item_to_cart()

    # Шаг 4: Переходим в корзину
    inventory_page.go_to_cart()

    # Шаг 5: Проверка наличия товара
    actual_items = cart_page.get_item_names_in_cart()
    assert actual_items == [expected_item], f"Expected {expected_item}, but got {actual_items}"
    logger.info("Assertion passed: item is in cart")

    # Шаг 6: Удаляем товар
    cart_page.click_remove_button()

    # Шаг 7: Проверка, что корзина пуста
    assert cart_page.is_cart_empty(), "Cart should be empty after removal"
    logger.info("Assertion passed: cart is empty")

    logger.info("=== Test passed ===")

def test_add_and_remove_item_from_cart_full_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Шаг 1: Открыть сайт и войти
    driver.get("https://www.saucedemo.com/v1/")
    login_page.login("standard_user", "secret_sauce")

    # ... остальной код теста
    # Шаг 2: Добавить первый товар
    first_item_name = inventory_page.get_first_item_name()
    inventory_page.add_first_item_to_cart()

    # Шаг 3: Перейти в корзину
    inventory_page.go_to_cart()

    # Шаг 4: Проверить содержимое корзины
    assert cart_page.get_item_names_in_cart() == [first_item_name]

    # Шаг 5: Удалить товар
    cart_page.click_remove_button()

    # Шаг 6: Проверить, что корзина пуста
    assert cart_page.is_cart_empty()