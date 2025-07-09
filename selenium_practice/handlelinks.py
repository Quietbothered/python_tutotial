# # links
# 1 internal link samer page
# 2 external link other page
# 3 broken link for future work

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()#maximize browser window


links = driver.find_elements(By.TAG_NAME, 'a')
print('total number of links', len(links))
for link in links :
    print (link.text)
    print(link.get_attribute('value'))

