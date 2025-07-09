
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()#maximize browser window
time.sleep(5)










