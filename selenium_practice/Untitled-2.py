
#Frames / IFrames
# ----------------------------
# switch_to.frame('name of frame')
# switch_to.frame('id of frame')
# switch_to.frame(webelement)
# switch_to.frame(0)

# frame iframe form 


import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
driver.maximize_window()#maximize browser window
time.sleep(4)
try:
    driver.switch_to.frame("frm1")
except Exception:
    print(f"error orccur in switching i frame")
# d;river.find_element(By.LINK_TEXT, )
try:
    drp_ele = driver.find_element(By.XPATH, '//*[@id="course"]')
except Exception :
    print(f"not found")
drp_val = Select(drp_ele)
drp_val.select_by_visible_text("Java")



time.sleep(4)





















