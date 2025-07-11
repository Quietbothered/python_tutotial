from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options= ops)



driver.get('https://whatmylocation.com/#google_vignette')
driver.maximize_window()

time.sleep(40)


