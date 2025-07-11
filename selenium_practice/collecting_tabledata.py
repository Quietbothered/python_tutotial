from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv_obj)


driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(3)
#login creditial//input[@placeholder="username"]
driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys('Admin')
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('admin123')
driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()

time.sleep(4)
driver.find_element(By.XPATH, '//aside[@class="oxd-sidepanel"]//li[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//span[normalize-space()="User Management"]').click()
wait = WebDriverWait(driver, 10)
dropdown_item = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='oxd-dropdown-menu']//li")))
dropdown_item.click()
time.sleep(2)

rows_list = driver.find_elements(By.XPATH, '//div[@class="oxd-table-body"]/div')

print('total number of rows : ',len(rows_list))

count = 0
for i in range(1,len(rows_list)+1):
    status = driver.find_element(By.XPATH,'//div[@class="oxd-table-body"]/div['+str(i)+']/div/div[5]')
    if status.text == 'Enabled':
        count+=1

print("total enabled users",count)

time.sleep(10)