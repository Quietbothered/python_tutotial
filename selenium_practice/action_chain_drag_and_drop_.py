#drag_and_drop_

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)


driver.get('https://demo.automationtesting.in/Static.html')
driver.maximize_window()
time.sleep(3)

src_ele = driver.find_element(By.XPATH, '//*[@id="dragarea"]/div[2]')
target_ele = driver.find_element(By.XPATH, '//*[@id="droparea"]')
act = ActionChains(driver)
act.drag_and_drop(src_ele, target_ele).perform()
