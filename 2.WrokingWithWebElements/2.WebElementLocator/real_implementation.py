import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Locator():

    def webelement_locator(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Element find By Name
        username_NAME = driver.find_element(By.NAME, 'username')
        if username_NAME is not None:
            print("Element Successfully found by Name")
        else:
            print("Element found Failure by name")

        # Element find By CSS
        username_CSS = driver.find_element(By.CSS_SELECTOR, "[name='username']")
        if username_CSS is not None:
            print("Element Successfully found by CSS")
        else:
            print("Element found Failure by CSS")

        # Element find By Xpath
        try:
            username_Xpath = driver.find_element(By.XPATH, "//input[@id='username']")
            if username_Xpath is not None:
                print("Element Successfully found by Xpath")
        except:
            print("Element found Failure by XPATH")

        driver.close()


test_object = Locator()
test_object.webelement_locator()
