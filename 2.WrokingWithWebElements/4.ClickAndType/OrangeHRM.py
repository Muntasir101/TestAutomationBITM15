import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class OrangeHRM_Login():

    def login_TC001(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Element Finds
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        login_btn = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        # Login Action
        username_field.clear()
        username_field.send_keys("Admin")
        time.sleep(2)
        password_field.clear()
        password_field.send_keys("admin123")
        time.sleep(2)
        login_btn.click()
        time.sleep(3)

        driver.close()


test_object = OrangeHRM_Login()
test_object.login_TC001()
