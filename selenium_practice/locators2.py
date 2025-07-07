from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)



driver.get("https://www.automationexercise.com/")
driver.maximize_window()#maximize browser window

slider = driver.find_elements(By.CLASS_NAME, "col-sm-6")
print(len(slider))


links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
