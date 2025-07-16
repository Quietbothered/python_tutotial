# double click action

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(12)

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame('iframeResult')
field = driver.find_element(By.XPATH , '//*[@id="field1"]')
field.clear()
field.send_keys("alpha beta gama")
act = ActionChains(driver)

button = driver.find_element(By.XPATH, '/html/body/button')
act.double_click(button).perform()

time.sleep(3)