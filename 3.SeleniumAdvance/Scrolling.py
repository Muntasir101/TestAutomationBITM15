import time
from selenium import webdriver


class Scroll():
    def page_scroll(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://apple.com")
        time.sleep(5)

        # Scroll down
        driver.execute_script("window.scrollBy(0,5000);")
        time.sleep(3)
        driver.get_screenshot_as_file("E:\\BITM_Online_15\\Screenshot\\Apple_footer.png")

        # Scroll up
        driver.execute_script("window.scrollBy(0,-5000);")
        time.sleep(3)
        driver.get_screenshot_as_file("E:\\BITM_Online_15\\Screenshot\\Apple_header.png")

        driver.close()


test_obj = Scroll()
test_obj.page_scroll()
