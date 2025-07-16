#upload files

from selenium import webdriver
from selenium.webdriver.common.by  import By

from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service(r"C:\Users\91878\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get('https://formstone.it/components/upload/demo/')
driver.maximize_window()
# form = driver.find_element(By.XPATH, '//*[@id="example-0"]/form')
# driver.switch_to.frame(form)
driver.find_element(By.XPATH, '//*[@id="example-0"]/form/div[1]/input').send_keys(r'C:\Users\91878\python_tutotial\web_table_data.txt')


time.sleep(5)