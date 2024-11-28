"""
This script prepares driver to work with demoqa.com
"""

from time import sleep
from selenium.webdriver import Chrome


def setup_driver():
    """Initializes the WebDriver."""
    return Chrome()


def open_site(driver, url):
    """Goes to website"""
    driver.get(url)


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/')
    sleep(1)


if __name__ == '__main__':
    main()