"""
This script tests radio button functionality on demoqa.com
"""

from time import sleep
from selenium.common.exceptions import NoSuchElementException
from test21 import setup_driver, open_site

RADIO_IMPRESSIVE_XPATH = '//label[@for="impressiveRadio"]'
RESULT_TEXT_XPATH = '//span[@class="text-success"]'


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/radio-button/')

    # Click 'Impressive' radio button
    driver.find_element('xpath', RADIO_IMPRESSIVE_XPATH).click()

    # Get sure 'Impressive' is selected
    result = driver.find_element('xpath', RESULT_TEXT_XPATH).text
    assert result == 'Impressive', f"Expected Impressive, got {result}"

    sleep(1)

if __name__ == '__main__':
    main()
