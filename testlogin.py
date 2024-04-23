from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
url = "https://emr.fortiseahk.com"  
for _ in range(20):      
  driver.get(url)
  driver.find_element(By.ID,"authUser").send_keys("admin")
  driver.find_element(By.ID,"clearPass").send_keys("Fortinet2020!!")
  driver.find_element(By.ID,"login-button").click()
driver.quit() 
