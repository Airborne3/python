import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)

username_input= driver.find_element(By)
password_input = driver.find_element(By)

username_input.click()
username_input.send_keys("Admin")
password_input.click()
password_input.send_keys("Admin123")
