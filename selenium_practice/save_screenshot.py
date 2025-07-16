
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
loc = os.getcwd()
from selenium.webdriver.chrome.service import Service


serv_obj = Service(r'C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
# implicitwait(10)
driver.save_screenshot(loc + "\\selenium_practice\\homepage.png")


# driver.get_screenshot_as_base64(loc, "\\selenium_practice\\homepage.png")
# driver.get_screenshot_as_file(loc, "\\selenium_practice\\homepage.png")


# driver.find_element(By.XPATH, '//a[normalize-space()="Register"]').send_keys(Keys.CONTROL+Keys.RETURN)
for i in range(100):
    driver.switch_to.new_window('window')
    driver.get('https://demo.nopcommerce.com/')
time.sleep(3)