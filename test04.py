### keyboard control for drop down list

from selenium import webdriver
from selenium.webdriver import Keys
from datetime import datetime
import time

base_url = 'https://www.saucedemo.com'
standard_user = 'standard_user'
password = 'secret_sauce'

driver = webdriver.Chrome()
driver.get(base_url)

print('Fill username')
username_element = driver.find_element(by='xpath', value='//input[@id="user-name"]')
username_element.send_keys(standard_user)

# print('Pause 1 second')
# time.sleep(1)

print('Fill password')
password_element = driver.find_element(by='xpath', value='//input[@id="password"]')
password_element.send_keys(password)

print('Send Return')
password_element.send_keys(Keys.RETURN)

print('Verify that we are at the right url...', end='')
assert 'https://www.saucedemo.com/inventory.html' == driver.current_url
print('Success')

filter_element = driver.find_element(by='xpath', value='//*[@id="header_container"]/div[2]/div/span/select')
filter_element.click()
time.sleep(1)
filter_element.send_keys(Keys.ARROW_DOWN)
filter_element.send_keys(Keys.RETURN)

print('Make screenshot and save it to the file')
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
driver.save_screenshot(f'./screenshots/screenshot_{current_datetime}.png')

time.sleep(2)
