import unittest
import time
from selenium import webdriver
from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils


class LoginTest(unittest.TestCase):
    def test_login_invalid(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Excel Implementation
        file = "E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Framework\\data\\test_data.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            login_page_obj = LoginPage(driver)
            login_page_obj.login_orange(username, password)

            if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
                excel_utils.write_data(file, sheet, r, 4, "Login")

            else:
                excel_utils.write_data(file, sheet, r, 4, "Not Login")

        driver.close()
