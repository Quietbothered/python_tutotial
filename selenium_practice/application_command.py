# 1 get command
# 2 conditional command
# 3 browser command
# 4 navigational command
# 5 wait command


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)



#application commands  
#get  title current_url page_source

driver.get("https://money.rediff.com/gainers/bse/daily/groupall")

print(driver.title)
print(driver.current_url)
print(driver.page_source)


























driver.quit()




