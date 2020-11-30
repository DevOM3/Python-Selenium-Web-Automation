import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")   # accessing the link on given text
link.click()    # clicking on the link

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    # element.clear() to clear the searchbar

    # going to the previous page
    driver.back()
    driver.back()
    driver.back()
    # going forward
    driver.forward()
except:
    driver.quit()
