
# #CONDITIONAL COMMAND through web elements only not through driver.is_display()
# is_displayed()
# is_enabled()
# is_selected()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

#code herer

# search_box = driver.find_element(By.XPATH, '//input[@id="small-searchterms"]')

# print(search_box.is_displayed())

# print(search_box.is_enabled())

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
print(rd_male.is_selected())

rd_male.click()
time.sleep(2)
print("after selecting")

# rd_male = driver.find_element(By.XPATH, '//span[@class="male"]/following::*')
print(rd_male.is_selected())

