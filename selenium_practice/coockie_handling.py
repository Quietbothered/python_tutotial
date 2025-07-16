
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


cookie = driver.get_cookies()
print("coolie dict length", len(cookie))

for i in cookie :
    print(i['name']+':')
    print(type(i.get('name')),':',i.get('secure'))
    pass


driver.add_cookie({"name": "mycookie",
    "value": "12345621",
    "secure": True})
cookie = driver.get_cookies()

print("coolie dict length new ", len(cookie))

for i in cookie :
    print(i['name']+':')
    print(type(i.get('name')),':',i.get('secure'))
    

# delete specific cookie 
driver.delete_cookie("mycookie")
cookie = driver.get_cookies()
print(len(cookie))
driver.delete_all_cookies()
cookie = driver.get_cookies()
print(len(cookie))
for i in cookie :
    print(i['name']+':')
    print(type(i.get('name')),':',i.get('secure'))
    