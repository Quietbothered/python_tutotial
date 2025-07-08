# #browser commands
# close() = always close 1 browser /tab at a time i.e parent tab/browser window(where driver focused)
# quit() = close multiple browser windows ()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Computers']" ).click()
driver.find_element(By.LINK_TEXT, "Computers").click()
time.sleep(5)


# driver.close()
driver.quit()





























