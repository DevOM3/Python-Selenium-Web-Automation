from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

driver = Chrome("chromedriver_win32/chromedriver.exe")
driver.get("https://www.onlinemictest.com/mouse-test/")

action = ActionChains(driver)
mouse = driver.find_element_by_id("mouse")
action.move_to_element(mouse)
action.perform()
while True:
    action.click()
    action.perform()

