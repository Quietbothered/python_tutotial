#we need to first install request package throutgh file setting projectinterpreter

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()#maximize browser window

alllinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0
for link in alllinks:
    url = link.get_attribute('href')
    try :
        
        res = requests.head(url)
    except:
        None
    if res.status_code>= 400:
        print(url, "  is broken link")
        count+=1
    else:
        print(url, "   is valid link")
        
print("total number of brokent links are ", count)



