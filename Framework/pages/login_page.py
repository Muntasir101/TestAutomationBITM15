import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        # Element Finds
        username_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')
        login_btn = self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        # Login Action
        username_field.clear()
        username_field.send_keys(username)
        time.sleep(2)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(2)

        login_btn.click()
        time.sleep(3)
