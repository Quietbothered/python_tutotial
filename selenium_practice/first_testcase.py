# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


# # Use raw string (r"...") to avoid escape sequence issues
# service = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# driver.find_element(By.NAME , "Username").send_keys("Admin")

# driver.find_element(By.NAME , "Password").send_keys("admin123")
# driver.find_element(By.XPATH, '//button[normalize-space()="Login"]')


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time  # Optional for delays

# Setup
service = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Optional wait for page to load
time.sleep(3)  # Or use WebDriverWait (recommended for dynamic pages)

# Fill login form
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()



act_title = driver.title 
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("login test pass")
else:
    print("login test fail")


