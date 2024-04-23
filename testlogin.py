from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
url = "https://<your url test"  
for _ in range(20):      
  driver.get(url)
  driver.find_element(By.ID,"authUser").send_keys("user")
  driver.find_element(By.ID,"clearPass").send_keys("pass")
  driver.find_element(By.ID,"login-button").click()
driver.quit() 
