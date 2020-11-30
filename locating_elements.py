from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys     # this gives access to physical keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")

driver.get("https://techwithtim.net")

search = driver.find_element_by_name("s")   # accessing element by Name
search.send_keys("test")    # type what you want to search
search.send_keys(Keys.RETURN)   # press return key to search


# waiting till the element searched is loaded
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()

driver.quit()
