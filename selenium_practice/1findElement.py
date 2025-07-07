from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()#maximize browser window

driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.LINK_TEXT, "Register").click()
sliders = driver.find_elements(By.TAG_NAME, "a")
print(len(sliders))
time.sleep(2)


#linktext and partial link text


# driver.find_element(By.LINK_TEXT, )








