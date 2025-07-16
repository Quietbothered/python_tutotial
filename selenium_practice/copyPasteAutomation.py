#copy paste automation
# 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get('https://text-compare.com/')
driver.maximize_window()

imput1 = driver.find_element(By.XPATH, '//*[@id="inputText1"]')
imput2 = driver.find_element(By.XPATH, '//*[@id="inputText2"]')
# driver.find_element(By.XPATH, "")
imput1.send_keys("jju2bijbrratatatata")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input 1 ---> copy  Copy TEXT

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#use tab to change box of input 
act.send_keys(Keys.TAB).perform()
# paste command
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(3)
