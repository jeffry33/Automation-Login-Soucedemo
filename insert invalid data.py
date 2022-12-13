from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time

driver.get("https://www.saucedemo.com/")
driver.find_element(By.NAME, "user-name").send_keys("jeffry")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.NAME, "login-button").click()
time.sleep(2)
driver.close()