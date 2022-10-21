import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Dropdown():

    def dropdown_options(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(5)

        dropdown = driver.find_element(By.CSS_SELECTOR, 'select#dropdown')
        all_options = Select(dropdown)

        # Select the option at the given index.
        #all_options.select_by_index(1)

        #all_options.select_by_value('2')

        all_options.select_by_visible_text('Option 1')

        time.sleep(5)

        driver.close()


test_object = Dropdown()
test_object.dropdown_options()
