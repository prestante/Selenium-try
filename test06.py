### login using imports & hidden menu touch

from selenium.webdriver import Chrome
from selenium.webdriver import Keys
import login
import time

driver = Chrome()
login.login(driver)

# time.sleep(1)
print('Click on the hidden menu button')
hidden_menu_button = driver.find_element(by='id', value='react-burger-menu-btn')
hidden_menu_button.click()

print('Wait')
time.sleep(1)

print('Check the hidden menu is open...', end='')
hidden_menu_container = driver.find_element(by='xpath', value='//*[@id="menu_button_container"]/div/div[2]')
assert 'false' == hidden_menu_container.get_attribute('aria-hidden')
print('OK')