"""
This script tests checkboxes functionality on demoqa.com
"""

from time import sleep
from test21 import setup_driver, open_site

EXPAND_ALL_BUTTON_XPATH = '//button[@aria-label="Expand all"]'
HOME_CHECKBOX_XPATH = '//label[@for="tree-node-home"]'
REACT_CHECKBOX_XPATH = '//label[@for="tree-node-react"]'
RESULT_FIELD_XPATH = '//div[@id="result"]'



def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/checkbox/')

    # Click Expand All button
    driver.find_element('xpath', EXPAND_ALL_BUTTON_XPATH).click()

    # Click Home checkbox to select them all
    driver.find_element('xpath', HOME_CHECKBOX_XPATH).click()

    # Click React checkbox to unselect it
    driver.find_element('xpath', REACT_CHECKBOX_XPATH).click()

    # Get all the resulting checks. Should be 13/17 as we deselected 1 which also removed 2 parent checks
    result_elements = driver.find_element('xpath', RESULT_FIELD_XPATH).find_elements('class name', 'text-success')
    assert len(result_elements) == 13, f"Expected to be 13 checks, but actually got {len(result_elements)}"

    sleep(1)


if __name__ == '__main__':
    main()
