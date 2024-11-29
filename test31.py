"""
This script tests sliders on https://datika.me/en/category/black-friday/
"""

import re
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test21 import setup_driver, open_site


def main():
    """Standalone usage for testing purposes."""
    driver = setup_driver()
    open_site(driver, 'https://datika.me/en/category/black-friday/')
    driver.maximize_window()

    actions = ActionChains(driver)
    driver.execute_script("window.scrollTo(0, 500);")

    sleep(1)

    # Find the handles
    handles = driver.find_elements(By.CSS_SELECTOR, ".ui-slider-handle")

    # Drag the first handle
    actions.click_and_hold(handles[0]).move_by_offset(40, 0).release().perform()

    sleep(1)
    
    # Drag the second handle
    actions.click_and_hold(handles[1]).move_by_offset(-40, 0).release().perform()

    sleep(1)

    # Read minimum and maximum price
    url = driver.current_url
    price_min_matches = re.findall(r"price_min=(\d+)", url)
    price_max_matches = re.findall(r"price_max=(\d+)", url)
    price_min = int(price_min_matches[0]) if price_min_matches else None
    price_max = int(price_max_matches[0]) if price_max_matches else None
    
    # Get all prices and check if neither of them is outside the range
    price_elements = driver.find_elements(By.XPATH, "//*[@class='price nowrap' or @class='price price-new nowrap']")
    prices = [int(re.sub(r'[ €,]', '', element.text)) for element in price_elements if element.text.strip()]
    print(prices)
    assert all(price_min <= price <= price_max for price in prices), f"Some prices are outside of {price_min} and {price_max}"


if __name__ == '__main__':
    main()
