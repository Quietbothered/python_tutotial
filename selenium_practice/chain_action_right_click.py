#right click 
# .context_click(nutton).perform()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)


driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
time.sleep(3)

button = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")
act = ActionChains(driver)
act.context_click(button).perform()
time.sleep(4)







