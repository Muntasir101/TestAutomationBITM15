import unittest
import time
from selenium import webdriver
from Framework.pages.login_page import LoginPage

class LoginTest(unittest.TestCase):
    def test_login_invalid(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        
        login_page_obj = LoginPage(driver)
        login_page_obj.login_orange("Admin", 'admin123')

