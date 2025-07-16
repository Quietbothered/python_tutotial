#slider element 
# .drag_and_drop_by_offset(element, xoffset,yoffset)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)


driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
driver.maximize_window()
time.sleep(3)

min = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
max = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')
print("location before moving")
print(min.location)
print(max.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min, 100,0).perform()
act.drag_and_drop_by_offset(max, -39,0).perform()

print("location after moving")
print(min.location)
print(max.location)
