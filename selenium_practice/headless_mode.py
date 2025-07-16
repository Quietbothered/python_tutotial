# headless mode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
loc = os.getcwd()


def headlessMode():
    
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service(r'C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    ops = webdriver.ChromeOptions()
    # ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options= ops )
    return driver 
driver = headlessMode()
driver.get('https://demo.nopcommerce.com/')
# driver.maximize_window()
print(driver.title)
print(driver.current_url)
