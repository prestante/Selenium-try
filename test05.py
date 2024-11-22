### scroll the page and hover the elements

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

print('Fill password')
password_element = driver.find_element(by='xpath', value='//input[@id="password"]')
password_element.send_keys(password)

print('Send Return')
password_element.send_keys(Keys.RETURN)

print('Verify that we are at the right url...', end='')
assert 'https://www.saucedemo.com/inventory.html' == driver.current_url
print('Success')

time.sleep(1)
print('Scroll to 0, 100')
driver.execute_script("window.scrollTo(0, 100);")
time.sleep(1)
print('Scroll by 0, -50')
driver.execute_script("window.scrollBy(0, -50);")
time.sleep(1)

red_tshirt_element = driver.find_element(by='xpath', value='//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
print('Scrolling to the Red T-shirt')
driver.execute_script("arguments[0].scrollIntoView();", red_tshirt_element)
time.sleep(2)