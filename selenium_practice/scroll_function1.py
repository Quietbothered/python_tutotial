from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)

driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()
time.sleep(3)
#  scroll by pixel
# driver.execute_script("window.scrollBy(0,3000)",'')
# print('yofset is ',end=' ')
# value = driver.execute_script('return window.pageYOffset;')
# print(value )
# scroll untill u find an element 
flag = driver.find_element(By.XPATH, '//img[@alt="Flag of India"]')
driver.execute_script('arguments[0].scrollIntoView();',flag)

value = driver.execute_script('return window.pageYOffset;')
print("wekfnoewfbow  ratqatatatattatatat :",value )

driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')


time.sleep(5)