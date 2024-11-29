"""
This script tests different things on automationpractice.com
"""

from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from test21 import setup_driver, open_site

DOUBLE_CLICK_BUTTON_XPATH = '//button[@id="doubleClickBtn"]'
RIGHT_CLICK_BUTTON_XPATH = '//button[@id="rightClickBtn"]'
LEFT_CLICK_BUTTON_XPATH = '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/button'


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/buttons/')

    actions = ActionChains(driver)

    # Double click corresponding button
    actions.double_click(driver.find_element('xpath', DOUBLE_CLICK_BUTTON_XPATH)).perform()

    # Right click corresponding button
    actions.context_click(driver.find_element('xpath', RIGHT_CLICK_BUTTON_XPATH)).perform()
    
    # Left click corresponding button
    actions.click(driver.find_element('xpath', LEFT_CLICK_BUTTON_XPATH)).perform()

    sleep(1)

if __name__ == '__main__':
    main()
