import time

from selenium import webdriver


class Firefox():

    def firefox_launch(self):
        driver = webdriver.Firefox(executable_path="")
        driver.get("http://localhost:80/orangehrm/web/index.php/auth/login")
        time.sleep(5)
        driver.close()


test_object = Firefox()
test_object.firefox_launch()
