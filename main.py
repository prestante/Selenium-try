from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()
#username_element = driver.find_element(by='name', value='user-name')
username_element = driver.find_element(by='xpath', value='//Input[@id="user-name"]')
username_element.send_keys('standard_user')

password_element = driver.find_element(by='id', value='password')
password_element.send_keys('secret_sauce')

time.sleep(1)
button_login_element = driver.find_element(by='xpath', value='//*[@name="login-button"]')
button_login_element.click()

#title = driver.title
#print(title)
time.sleep(1)