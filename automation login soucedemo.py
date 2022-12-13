from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time

driver.get("https://www.saucedemo.com/")
driver.find_element(By.NAME, "user-name").send_keys("problem_user")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.NAME, "login-button").click()
time.sleep(2)
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(4)
driver.close()