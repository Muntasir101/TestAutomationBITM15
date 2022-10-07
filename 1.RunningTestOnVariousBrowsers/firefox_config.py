import time

from selenium import webdriver


class Firefox():

    def firefox_launch(self):
        driver = webdriver.Firefox(executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("http://google.com")
        time.sleep(5)
        driver.close()


test_object = Firefox()
test_object.firefox_launch()
