import time
from selenium import webdriver


class Screenshot():
    def capture_screenshot(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://google.com")
        time.sleep(5)

        driver.get_screenshot_as_file("E:\\BITM_Online_15\\Screenshot\\Google.png")

        driver.close()


test_obj = Screenshot()
test_obj.capture_screenshot()
