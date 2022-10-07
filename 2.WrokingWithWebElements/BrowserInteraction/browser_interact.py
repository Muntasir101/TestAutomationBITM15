from selenium import webdriver
import time


class BrowserInteraction():
    def browser_interaction_commands(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\"
                            "Drivers\\geckodriver.exe")
        driver.get("http://google.com")

        title = driver.title
        print(title)

        currentUrl = driver.current_url
        print(currentUrl)

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        driver.back()
        time.sleep(3)

        driver.forward()
        time.sleep(2)

        driver.refresh()

       # driver.close()
        driver.quit()


test_object = BrowserInteraction()
test_object.browser_interaction_commands()
