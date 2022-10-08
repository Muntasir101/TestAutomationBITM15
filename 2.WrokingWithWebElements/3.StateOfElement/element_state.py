import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState():

    def webelement_state(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # Element find By Name
        username_field = driver.find_element(By.NAME, 'username')

        # Username field State: Displayed or Not. If not displayed return False
        username_display_status = username_field.is_displayed()
        print(username_display_status)

        # Username field State: Enabled or Not. If not displayed return False
        username_enable_status = username_field.is_enabled()
        print(username_enable_status)

        if username_display_status == True and username_enable_status == True:
            print('Username field is ready for testing.We can Start')
        else:
            print('Username field is not ready for testing.Bug found !!!')

        driver.close()


test_object = ElementState()
test_object.webelement_state()
