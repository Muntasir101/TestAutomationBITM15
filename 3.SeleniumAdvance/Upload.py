import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class UploadFile():
    def uploading(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(5)

        choose_file_btn = driver.find_element(By.CSS_SELECTOR, 'input#file-upload')
        choose_file_btn.send_keys("E:\\BITM_Online_15\\Screenshot\\Apple_footer.png")
        time.sleep(3)

        upload_btn = driver.find_element(By.CSS_SELECTOR, 'input#file-submit')
        upload_btn.click()
        time.sleep(3)

        driver.close()


test_obj = UploadFile()
test_obj.uploading()