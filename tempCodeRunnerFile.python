from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#select specific checkbox from list

# driver.find_element(By.XPATH, '//input[@id="checkBoxOption1"]').click()
#select all check boxes


checkboxes = driver.find_elements(By.XPATH, '//input[@type = "checkbox"]')
print("all check boxes are      ",len(checkboxes))

# for i in range(len(checkboxes)):
#     checkboxes[i].click()
    

# aproach 2
for checkbox in checkboxes:
    checkbox.click()
    
    


#3 selewct multiple check boxes using condition
for checkbox in checkboxes:
    optname = checkbox.get_attribute('id')
    
    if optname == 'checkBoxOption1' or optname == 'checkBoxOption2' :
        
        checkbox.click()
    
#4 select last 2 checkboxes
# n-2 i.e total length -2

for i in range (len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()


#  clearing all the check boxes

time.sleep(2)

for i in range (len(checkboxes)):
    if checkboxes[i].is_selected():
        
        checkboxes[i].click()


time.sleep(4)
