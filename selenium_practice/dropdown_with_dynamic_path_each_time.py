# bootstrap dropdown

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service

serv_obj = Service(r'C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="billing_country_field"]/span/span').click()
time.sleep(3)
contry_lis = driver.find_elements(By.XPATH, '//*[@id="select2-billing_country-results"]//li')
print(contry_lis[103].text)
for country in contry_lis:
    if country.text.strip().lower() == "india": #is it case sensitive
        country.click()
    # print(type(country.text))
    # print(country.text)
        print('we clicked the element')
# time.sleep(3)



# what is wrong here we need to call the list element each time in for loop since so that we dont get stale element error










