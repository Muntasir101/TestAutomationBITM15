import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Alert():
    def alert_handle(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(5)

        normal_alert = driver.find_element(By.CSS_SELECTOR, "[onclick='jsAlert\(\)']")
        normal_alert.click()
        driver.switch_to.alert.accept()
        time.sleep(5)

        confirm_alert = driver.find_element(By.XPATH, "//div[@id='content']//ul//button[.='Click for JS Confirm']")
        confirm_alert.click()
        driver.switch_to.alert.dismiss()
        time.sleep(5)

        prompt_alert = driver.find_element(By.XPATH, "//div[@id='content']//ul//button[.='Click for JS Prompt']")
        prompt_alert.click()
        driver.switch_to.alert.send_keys('Test Message')
        driver.switch_to.alert.accept()
        time.sleep(5)

        driver.close()


test_obj = Alert()
test_obj.alert_handle()
