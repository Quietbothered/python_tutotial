#drop down




import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()#maximize browser window
time.sleep(4)
drpcountry_ele = driver.find_element(By.XPATH, '//*[@id="dropdown-class-example"]')
drpcountry = Select(drpcountry_ele)
#select element from drop down

drpcountry.select_by_visible_text('Option2')
# drpcountry.select_by_value('Option3') #argentina
# drpcountry.select_by_index(13) #index not to be put in doub;le quotation



alloptions = drpcountry.options
print(len(alloptions), "are tital no of options")

for opt in alloptions:
    print(opt.text)
    
    
#select option without using built in function
for opt in alloptions:
    if opt.text == "Option2":
        opt.click()
        break
