# self 
# parent
# child
# ancestor
# descendant 
# following
# following sibling
# preceding
# preceding sibling

# // *[attribute = 'value']/child::tagname
# //*[attribute = 'value']/following :: tagname
# //xpath of element /following-sibling::sibling tag [@attribute = value]


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time

serv_obj = Service(r"C:\Driver\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
driver.maximize_window()

#self

# text_element = driver.find_element(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/self::a').text
# print(text_element)

#parent

# text_element = driver.find_element(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/parent::td').text
# print(text_element)

# #child emlement

# text_element = driver.find_elements(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/ancestor::tr/child::td')
# print(len(text_element))
# for i in range(len(text_element)):
    
#     print(text_element[i].text)

# # ancestor

# text_element = driver.find_element(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/ancestor :: tr').text
# print(text_element)

# descedent

# text_element = driver.find_elements(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/ancestor::tr/descendant::*')
# print('number of descendant are ',len(text_element))

# #following
# text_element = driver.find_elements(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/ancestor::tr/following::*')
# print('number of following are ',len(text_element))


# # following sibling
# text_element = driver.find_elements(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/ancestor::tr/following-sibling::*')
# print('number of following siblings are ',len(text_element))


#presceding


text_element = driver.find_elements(By.XPATH, '//a[normalize-space()="Peninsula Land L"]/ancestor::tr/preceding::*')
print('number of presceding siblings are ',len(text_element))
