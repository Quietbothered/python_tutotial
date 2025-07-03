from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class demoFindelement():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID ,"login-input" ).send_keys("test@test.com")
        

findbyid = demoFindelement()
findbyid.locate_by_id_demo()





