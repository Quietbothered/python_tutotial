#how to switch between browser window
# -----------------------------------
# switch_to(windowID)
# current_window_handle -> Return window id of single window
#window_handles --> return window id of multiple browser windows



# import requests as requests
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
# time.sleep(3)
mywait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions= [NoSuchElementException])

# windowid = driver.current_window_handle
# print("windowid is",  windowid)  #12DD75124652DC0E142B108A4E3B7B2F                        
#                                 #1D2A618540EDF6EAB58B5B8DC48EE7EF

sel = mywait.until(ec1.presence_of_element_located((By.LINK_TEXT, 'OrangeHRM, Inc')))
sel.click()



window_ids = driver.window_handles
# for i in window_ids:
print("parent id",window_ids[0])
print("child id",window_ids[1])

time.sleep(90)


# driver.close()

# driver.switch_to(windowID)
# chat gpt code below 


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import (NoSuchAttributeException, NoSuchElementException)


# # Start the Chrome driver
# serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

# # Step 1: Open the OrangeHRM login page
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()

# # Step 2: Wait for page to load (static wait or use WebDriverWait instead)
# time.sleep(3)
# mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException])
# # Step 3: Click the link that opens a new window/tab
# driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()

# # Step 4: Get window handles
# window_ids = driver.window_handles
# parent_id = window_ids[0]
# child_id = window_ids[1]

# print("Parent Window ID:", parent_id)
# print("Child Window ID:", child_id)

# # Step 5: Switch to the new window (child)
# driver.switch_to.window(child_id)
# print("Switched to child window:", driver.title)

# time.sleep(3)  # Let it load and be visible

# # Step 6: Close child window
# driver.close()

# # Step 7: Switch back to parent window
# driver.switch_to.window(parent_id)
# print("Switched back to parent:", driver.title)

# # Optional cleanup
# time.sleep(2)
# driver.quit()
