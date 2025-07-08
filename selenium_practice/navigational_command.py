# # navigatinal command   
# 1 back()
# 2 forward()
# 3 refresh()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.back()
driver.forward()
driver.refresh()
driver.quit()



