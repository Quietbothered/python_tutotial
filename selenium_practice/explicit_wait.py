# # explicit wait
#     More effectively  works
#     but 
#     multiple places
        # feel dificulty







from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec1
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException
)



serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# mywait = WebDriverWait(driver, 100) #explicit wait declaration

mywait = WebDriverWait(driver, 10,poll_frequency= 2, ignored_exceptions=[NoSuchElementException,
                                                       ElementNotVisibleException,
                                                       ElementNotSelectableException,
                                                       Exception])

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(ec1.presence_of_element_located((By.XPATH, '//h3[normalize-space()="Selenium"]'))) 
searchlink.click()
time.sleep(4)
driver.quit()


