"""
This module contains the login function.
"""

from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
import config


USERNAME_XPATH = '//input[@id="user-name"]'
PASSWORD_XPATH = '//input[@id="password"]'
LOGIN_BUTTON_XPATH = '//input[@id="login-button"]'


def login(driver):
    """
    Logs into the application using credentials from the config module.
    """
    try:
        # Open the base URL
        driver.get(config.base_url)

        # Enter username and password
        driver.find_element(by='xpath', value=USERNAME_XPATH).send_keys(config.standard_user)
        driver.find_element(by='xpath', value=PASSWORD_XPATH).send_keys(config.standard_password)

        # Click the login button
        driver.find_element(by='xpath', value=LOGIN_BUTTON_XPATH).click()

        # Verify successful login
        assert "inventory" in driver.current_url, "Login failed: Unexpected URL"
        print("Login successful.")

    except NoSuchElementException as e:
        raise Exception("Login failed: Element not found.") from e


if __name__ == "__main__":
    # Run standalone
    driver = Chrome()
    try:
        login(driver)
    finally:
        driver.quit()