import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkbox():
    def checkbox_select(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(5)

        checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
        checkbox1.click()
        time.sleep(4)

        checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")
        checkbox2.click()
        time.sleep(2)

        driver.close()


test_obj = Checkbox()
test_obj.checkbox_select()
