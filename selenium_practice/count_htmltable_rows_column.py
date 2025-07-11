
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec1

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait        import WebDriverWait

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#  count number of rows in a web table
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()



time.sleep(4)
no_of_col = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[1]/th')
no_rows = driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr")

for i in no_of_col:
    print(i.text)
    

for i in no_rows:
    print(i.text)
    
print(len(no_of_col))
print('rows',len(no_rows))



# how to read proper table content of specific row or column



