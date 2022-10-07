from selenium import webdriver


class Chrome():
    def chrome_launch(self):
        driver = webdriver.Chrome(executable_path="E:\\BITM_Online_15\\Projects"
                                                  "\\TestAutomationBITM15\\Drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://apple.com")


test_object = Chrome()
test_object.chrome_launch()
