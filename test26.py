"""
This script tests exceptions, waits and expected conditions using delayed-appear element on demoqa.com
"""

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from test21 import setup_driver, open_site

VISIBLE_AFTER_XPATH = '//button[@id="visibleAfter"]'


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/dynamic-properties')

    max_retries = 7
    retries = 0
    timeout = 1

    while retries < max_retries:
        try:
            # Wait until the element is visible
            wait = WebDriverWait(driver, timeout=timeout)
            visible_after_5s_element = wait.until(
                EC.visibility_of_element_located(('xpath', VISIBLE_AFTER_XPATH))
            )
            assert visible_after_5s_element.text == 'Visible After 5 Seconds', (
                f"Expected 'Visible After 5 Seconds', got {visible_after_5s_element.text}"
            )
            print("Test passed: Element became visible.")
            break  # Exit loop if the test passed
        except TimeoutException:
            print(f"Retry {retries}/{max_retries}: Element not visible within {timeout} seconds. Refreshing page...")
            driver.refresh()
            retries += 1
            timeout += 1
    else:
        raise Exception("Test failed: Element did not become visible after maximum retries.")

    sleep(1)
    driver.quit()

if __name__ == '__main__':
    main()