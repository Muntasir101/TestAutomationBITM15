import time
from selenium import webdriver


class HeadlessTest():
    def firefox_headless(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True

        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe",
            options=firefox_options)

        driver.get("https://www.google.com")
        time.sleep(3)

        print(driver.title)

        driver.close()


test_obj = HeadlessTest()
test_obj.firefox_headless()
