import config
# from selenium import webdriver

def login(driver):
    # driver = webdriver.Chrome()
    driver.get(config.base_url)
    # driver.maximize_window()

    print('Filling username')
    username_element = driver.find_element(by='xpath', value='//input[@id="user-name"]')
    username_element.send_keys(config.standard_user)

    print('Filling password')
    password_element = driver.find_element(by='xpath', value='//input[@id="password"]')
    password_element.send_keys(config.standard_password)

    print('Clicking Login button')
    button_login_element = driver.find_element(by='xpath', value='//input[@id="login-button"]')
    button_login_element.click()

    print('Verifying that we are at the right url...', end='')
    assert 'https://www.saucedemo.com/inventory.html' == driver.current_url
    print('OK')
