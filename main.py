import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

product=driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text

if product=='Products':
    print('Login was successful')
    assert True
else:
    print('Login was not successful')
    assert False



time.sleep(5)