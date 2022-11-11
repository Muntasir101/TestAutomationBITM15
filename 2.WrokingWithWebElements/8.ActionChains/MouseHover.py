import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MouseHover():
    def hover(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://demo.opencart.com/")
        time.sleep(5)

        actions = ActionChains(driver)

        desktop = driver.find_element(By.LINK_TEXT, 'Desktops')

        # Hover to Desktop menu
        actions.move_to_element(desktop).perform()
        time.sleep(3)

        mac = driver.find_element(By.LINK_TEXT, 'Mac (1)')
        mac.click()
        time.sleep(5)

        driver.close()


test_obj = MouseHover()
test_obj.hover()
