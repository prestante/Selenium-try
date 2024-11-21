### keyboard control and expected error

from selenium import webdriver
from selenium.webdriver import Keys
import time

base_url = 'https://www.saucedemo.com'
standard_user = 'standard_user'
password = 'secret_sauce'

driver = webdriver.Chrome()
driver.get(base_url)

print('Fill username')
username_element = driver.find_element(by='xpath', value='//input[@id="user-name"]')
username_element.send_keys(standard_user)

print('Pause 1 second')
time.sleep(1)

print('Send Backspace')
username_element.send_keys(Keys.BACKSPACE)

print('Fill password')
password_element = driver.find_element(by='xpath', value='//input[@id="password"]')
password_element.send_keys(password)

print('Pause 1 second')
time.sleep(1)

print('Click Login button')
button_login_element = driver.find_element(by='xpath', value='//input[@id="login-button"]')
button_login_element.click()

# print('Send Return')
# password_element.send_keys(Keys.RETURN)

print('Check if we got an error...',end='')
try:
    error_message_element = driver.find_element(by='xpath', value='//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert 'Epic sadface' in error_message_element.text
    print('Success')
except Exception as e:
    print(str(e).split(":")[0] + ": " + str(e).split(":")[1].strip())
    pass
