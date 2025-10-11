import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # Запуск браузера
driver.get("https://www.google.com/")

time.sleep(30)
element = driver.find_element(By.NAME,"q" )

element.click()
element.send_keys("лошадь")

driver.quit()

