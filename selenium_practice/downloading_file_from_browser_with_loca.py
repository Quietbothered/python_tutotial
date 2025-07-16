#downloading file from browser with location same as current directory

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os
loc = os.getcwd()
print(loc)
def chrome_setup():
    from selenium.webdriver.chrome.service import  Service
    serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    
    # download file on desired location
    # preferences = {"download.default_directory":r"C:\Users\91878\python_tutotial\selenium_practice"}
    preferences = {"download.default_directory":f'{loc}\selenium_practice', "plugins.always_open_document_externally":True}
    
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    
    
    
    
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver = chrome_setup()
driver.get('https://www.examplefile.com/document/pdf/1-mb-pdf')
driver.maximize_window()
flag = driver.find_element(By.XPATH, '//a[normalize-space()="Download"]')
driver.execute_script('arguments[0].scrollIntoView();',flag)
driver.find_element(By.XPATH, '//a[normalize-space()="Download"]').click()
time.sleep(3)
# driver.close()
#
