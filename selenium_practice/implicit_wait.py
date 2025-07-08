#wait command 
# 1 implicit wait
#  driver.implicit_wait(time)
        # single statement
        # performance will not redice (if element is available within time it will proceed to execute further statement
        # dis adv
        # if element is not available in 10 sec  , still there are chance of getting Exception
        




# 2 explicit wait 
        # work based on condition






# time.sleep(time) python function
        # simple to use 
        # but 
        # performance of script is poor 
        # if element is not available in 10 sec  , still there are chance of getting Exception
        



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
###########################################################################

driver.implicitly_wait(10) # seconds it is applicablt for all following statements

########################################################################


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#####################  find element() return single webelement
#1> locator matching with 1 web element
element = driver.find_element(By.XPATH, "//input[@id = 'small-searchterms']")
element.send_keys("apple macbook pro")


# element = driver.find_element(By.XPATH, "//div[@class = 'footer']//a").text



######### find_elements  teturn multiple elements

# 1 locator matching 1 webelement
# element = driver.find_elements(By.XPATH, "//input[@id = 'small-searchterms']")
# print(len(element)) 
# element[0].send_keys("apple macbook pro")

######### text vs get_attribute 
# text ---- return inner text of element of element
# get_attribute ------ return value of any attribute of web element if we write class insted of value it will return its class

print("it returns inner text",element.text)



print("values of element are ",element.get_attribute('value'))

time.sleep(3)














