"""
This script tests choose file form on demoqa.com
"""

from time import sleep
from os.path import basename
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test21 import setup_driver, open_site

CHOOSE_FILE_BUTTON_XPATH = '//input[@id="uploadFile"]'
UPLOADED_FILE_XPATH = '//p[@id="uploadedFilePath"]'


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://demoqa.com/upload-download/')

    # Absolute path to the file to be uploaded
    file_path = "/Users/pres/Downloads/MaSaSeDa.jpeg"
    filename = basename(file_path)  # Extract filename

    # Upload the file by sending the path to the file input element
    file_input = driver.find_element('xpath', CHOOSE_FILE_BUTTON_XPATH)
    file_input.send_keys(file_path)

    # Wait until the uploaded file path element is visible
    wait = WebDriverWait(driver, timeout=10)  # 10 seconds timeout
    uploaded_file_element = wait.until(
        EC.visibility_of_element_located(('xpath', UPLOADED_FILE_XPATH))
    )
    assert filename in uploaded_file_element.text, f"Expected {filename} in {uploaded_file_element.text}"

    sleep(1)

    driver.quit()

if __name__ == '__main__':
    main()