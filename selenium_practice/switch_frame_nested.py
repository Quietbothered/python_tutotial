
# import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver.support.ui import WebDriverWait
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()#maximize browser window
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe ')
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys('welcome')

driver.switch_to.parent_frame()#directlty switch to parent frame


time.sleep(4)


