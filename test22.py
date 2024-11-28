"""
This script tests checkboxes functionality on demoqa.com
"""

from time import sleep
from selenium.common.exceptions import NoSuchElementException
from test21 import setup_driver, open_site


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/checkbox/')

    # Click Expand All button
    driver.find_element('xpath', '//*[@id="tree-node"]/div/button[1]').click()

    # Click Home checkbox to select them all
    driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/span/label/span[1]').click()

    # Click React checkbox to unselect it
    driver.find_element('xpath', '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[1]/ol/li[1]/span/label/span[1]').click()

    # Get all the resulting checks. Should be 13/17 as we deselected 1 which also removed 2 parent checks
    result_elements = driver.find_element('xpath', '//*[@id="result"]').find_elements('class name', 'text-success')
    assert len(result_elements) == 13, f"Expected to be 13 checks, but actually got {len(result_elements)}"


if __name__ == '__main__':
    main()
