#aproach 2
# for handling browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec1

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait        import WebDriverWait

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()#maximize browser window

time.sleep(5)

driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()



window_ids = driver.window_handles
# for i in window_ids:
print("parent id",window_ids[0])
print("child id",window_ids[1])

# for wind in window_ids:
#     driver.switch_to.window(wind)
#     print(driver.title)

for wind in window_ids:
    driver.switch_to.window(wind)
    if driver.title == "OrangeHRM" :
        
        driver.close()

time.sleep(4)










