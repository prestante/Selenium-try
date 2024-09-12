### positive login testing

from selenium import webdriver
import time

base_url = 'https://www.saucedemo.com'
standard_user = 'standard_user'
password = 'secret_sauce'

driver = webdriver.Chrome()
driver.get(base_url)
driver.maximize_window()

print('Fill username')
username_element = driver.find_element(by='xpath', value='//input[@id="user-name"]')
username_element.send_keys(standard_user)

print('Fill password')
password_element = driver.find_element(by='xpath', value='//input[@id="password"]')
password_element.send_keys(password)

print('Pause 1 second')
time.sleep(1)

print('Click Login button')
button_login_element = driver.find_element(by='xpath', value='//input[@id="login-button"]')
button_login_element.click()

# print('Verifying that the Products element text is "Products"...', end='')
# text_products_element = driver.find_element(by='xpath', value='//*[@id="header_container"]/div[2]/span')
# text_products_element_text = text_products_element.text
# assert text_products_element_text == 'Products'
# print('Done')

print('Verifying that we are at the right url...', end='')
url_expected = 'https://www.saucedemo.com/inventory.html'
url_received = driver.current_url
assert url_expected == url_received
print('Success')
