# tests/test_cart_full_flow.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_and_remove_item_from_cart_full_flow(driver):
    BASE_URL = "https://www.saucedemo.com/v1/"

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Шаг 1: Открыть сайт и войти
    login_page.open(BASE_URL)
    login_page.login("standard_user", "secret_sauce")

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