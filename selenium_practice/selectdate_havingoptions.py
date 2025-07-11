
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec1

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait        import WebDriverWait
from selenium.webdriver.support.select import Select
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
#  count number of rows in a web table
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

time.sleep(4)

driver.find_element(By.XPATH, '//input[@id="dob"]').click()
a = 'Aug'
b = '2022'
c = '13'



month_pick = Select(driver.find_element(By.XPATH, '//select[@aria-label="Select month"]'))
month_pick.select_by_visible_text(a)


year_pick = Select(driver.find_element(By.XPATH, '//select[@aria-label="Select year"]'))
year_pick.select_by_visible_text(b)

date_pick = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for date in date_pick:
    
    if date.text == '13':
        date.click()
        
time.sleep(8)



