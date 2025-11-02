import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_complete_checkout_flow(driver):
    time.sleep(2)

    # Arrange
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_one = CheckoutStepOnePage(driver)
    checkout_two = CheckoutStepTwoPage(driver)
    checkout_complete = CheckoutCompletePage(driver)

    # Act & Assert
    login_page.login("standard_user", "secret_sauce")
    time.sleep(1)

    # Добавляем первый товар
    first_item = driver.find_element("class name", "inventory_item_name").text
    inventory_page.add_first_item_to_cart()
    time.sleep(1)

    inventory_page.go_to_cart()
    time.sleep(1)

    # Проверяем, что товар в корзине
    cart_items = cart_page.get_item_names_in_cart()
    assert cart_items == [first_item], f"Ожидался товар: {first_item}, найдено: {cart_items}"
    time.sleep(1)

    # Переходим к оформлению
    cart_page.click_checkout()
    time.sleep(1)

    # Заполняем данные покупателя
    checkout_one.fill_checkout_info("John", "Doe", "12345")
    checkout_one.click_continue()
    time.sleep(1)

    # Проверяем товар и сумму на странице подтверждения
    overview_items = checkout_two.get_item_names()
    assert overview_items == [first_item], f"Товар не совпадает на странице Overview: {overview_items}"
    total = checkout_two.get_total_price()
    assert "Total:" in total, f"Итоговая сумма не найдена. Получено: {total}"
    time.sleep(1)

    # Завершаем заказ
    checkout_two.click_finish()
    time.sleep(1)

    # Проверяем финальное подтверждение
    header = checkout_complete.get_complete_header_text()
    assert header == "THANK YOU FOR YOUR ORDER", f"Неверный заголовок: {header}"

    # (опционально) Возвращаемся на главную
    checkout_complete.click_back_home()
    time.sleep(1)

    # Проверяем, что товар в корзине
    assert cart_page.get_item_names_in_cart() == [first_item]

    # Переходим к оформлению
    cart_page.click_checkout()

    # Заполняем данные покупателя
    checkout_one.fill_checkout_info("John", "Doe", "12345")
    checkout_one.click_continue()

    # Проверяем товар и сумму на странице подтверждения
    assert checkout_two.get_item_names() == [first_item]
    assert "Total:" in checkout_two.get_total_price()

    # Завершаем заказ
    checkout_two.click_finish()

    # Проверяем финальное подтверждение
    assert checkout_complete.get_complete_header_text() == "THANK YOU FOR YOUR ORDER"

    # (опционально) Возвращаемся на главную
    checkout_complete.click_back_home()