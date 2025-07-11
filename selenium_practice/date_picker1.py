#date picker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
import time

serv_obj = Service('C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()


year = "2027"
month = "August"
date = '25'

driver.switch_to.frame(0)
driver.find_element(By.XPATH, '//*[@id="datepicker"]').click()

while True:
    yr = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    mon = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    if month == mon and yr == year :
        break
    else :
        
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click()
        # driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click()

# select elements

dates = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]//table/tbody/tr/td/a')
for element in dates:
    if element.text == date:
        element.click()
        break

time.sleep(4)

