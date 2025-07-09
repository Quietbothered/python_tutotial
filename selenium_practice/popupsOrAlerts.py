# popups or alerts
# ----------------------
# js alert
# click for js confirm
# js prompt


# authentication pop ups
# -------------------------
# syntax http://username:password@actual url.com i.e
# http://admin:admin@the-internet.herokuapp.com/javascript_alerts 


#Frames / IFrames
# ----------------------------
# 


import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()#maximize browser window

driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()


alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys('hola its sent by me')
# alertwindow.accept()
alertwindow.dismiss()


time.sleep(4)







