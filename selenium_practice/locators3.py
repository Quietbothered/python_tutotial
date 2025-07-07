from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()#maximize browser window

# # tag and id

# #    tagname#value of id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('abc')
# #   tag and class 
# #    tagname.value of class 
# # input.inputtext_
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys('abc')
# # if no tag is there you can skipp it but . or # shpuld be present in syntax
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys('abc')

#  tag attribute tagname[attribute = value]   input[data-testid= "royal_email"]
driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal-email"]').send_keys("abc@gmail.com")

# driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("abc@gmail.com")

driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal-pass"]').send_keys("abc@gmail.com")


time.sleep(2)