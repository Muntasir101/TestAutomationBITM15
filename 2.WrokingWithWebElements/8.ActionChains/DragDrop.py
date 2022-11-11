import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DragDrop():
    def dragAndDrop(self):
        driver = webdriver.Firefox(
            executable_path="E:\\BITM_Online_15\\Projects\\TestAutomationBITM15\\Drivers\\geckodriver.exe")
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(5)

        actions = ActionChains(driver)

        driver.switch_to.frame(0)

        source = driver.find_element(By.ID, 'draggable')
        target = driver.find_element(By.ID, 'droppable')

        actions.drag_and_drop(source, target).perform()
        time.sleep(3)

        driver.close()


test_obj = DragDrop()
test_obj.dragAndDrop()
