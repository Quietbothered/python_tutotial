from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Setup
serv_obj = Service(r'C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()
time.sleep(3)

# Open dropdown
driver.find_element(By.XPATH, '//*[@id="billing_country_field"]/span/span').click()
time.sleep(2)

# Wait until elements are loaded (better with WebDriverWait in real use)
country_xpath = '//*[@id="select2-billing_country-results"]/li'

# Loop and click India
for i in range(249):  # Max 100 iterations just in case
    countries = driver.find_elements(By.XPATH, country_xpath)
    if i >= len(countries):
        break
    try:
        if countries[i].text.strip().lower() == "india":
            countries[i].click()
            print("Clicked India.")
            break
    except Exception as e:
        print("Retrying due to error:", e)
        time.sleep(0.5)  # Small delay before retry
