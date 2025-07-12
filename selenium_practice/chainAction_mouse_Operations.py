# mouse  Operations


# action chain operations
# ------------------------------------
# mouse hover  move_to_element(element like a b c)
# right click 
# double click 

# drzag and drop




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)


driver.get('https://demo.automationtesting.in/WebTable.html')
driver.maximize_window()
time.sleep(3)

a = driver.find_element(By.XPATH, '//a[normalize-space()="Interactions"]')
b = driver.find_element(By.XPATH, '//a[normalize-space()="Drag and Drop"]')
c = driver.find_element(By.XPATH, '//a[normalize-space()="Static"]')

#mouse hover movement
act = ActionChains(driver)

act.move_to_element(a).move_to_element(b).move_to_element(c).click().perform()

time.sleep(3)
