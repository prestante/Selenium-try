"""
This script tests the checkout process, using test11 components for preparation.
"""

import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from test11 import setup_driver, login_user, add_product_to_cart, go_to_cart, verify_cart_contents


CHECKOUT_BUTTON_XPATH = '//*[@id="checkout"]'
CHECKOUT_ITEM_TITLE_XPATH = '//*[@id="item_0_title_link"]/div'
CHECKOUT_ITEM_PRICE_XPATH = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
CHECKOUT_FINISH_MESSAGE_XPATH = '//*[@id="checkout_complete_container"]/h2'


def proceed_to_checkout(driver):
    """Proceeds to the checkout process."""
    try:
        driver.find_element(By.XPATH, CHECKOUT_BUTTON_XPATH).click()
    except NoSuchElementException as e:
        raise Exception("Checkout button not found.") from e


def fill_checkout_form(driver, first_name, last_name, postal_code):
    """Fills out the checkout form and continues."""
    try:
        driver.find_element(By.ID, 'first-name').send_keys(first_name)
        driver.find_element(By.ID, 'last-name').send_keys(last_name)
        driver.find_element(By.ID, 'postal-code').send_keys(postal_code)
        driver.find_element(By.ID, 'continue').click()
    except NoSuchElementException as e:
        raise Exception("Checkout form elements not found.") from e


def verify_order_summary(driver, product):
    """Verifies the order summary details."""
    try:
        summary_title = driver.find_element(By.XPATH, CHECKOUT_ITEM_TITLE_XPATH)
        summary_price = driver.find_element(By.XPATH, CHECKOUT_ITEM_PRICE_XPATH)
    except NoSuchElementException as e:
        raise Exception("Order summary not found.") from e

    assert summary_title.text == product.name, f"Expected summary title {product.name}, got {summary_title.text}"
    assert summary_price.text == product.price, f"Expected summary price {product.price}, got {summary_price.text}"


def finish_checkout(driver):
    """Click Finish button, check 'thanks' message and click Back Home button"""
    try:
        driver.find_element(By.ID, 'finish').click()
        finish_message = driver.find_element(By.XPATH, CHECKOUT_FINISH_MESSAGE_XPATH)
        assert finish_message.text == 'Thank you for your order!', f"Expected finish message 'Thank you for your order!', got {finish_message.text}"
        driver.find_element(By.ID, 'back-to-products').click()
    except NoSuchElementException as e:
        raise Exception("Cannot find Finish and/or Back Home button") from e


def main():
    """Tests the checkout process."""
    driver = setup_driver()
    login_user(driver)

    # Preparation step: Add a product to the cart
    product = add_product_to_cart(driver)
    go_to_cart(driver)
    verify_cart_contents(driver, product)

    # Proceed to checkout
    proceed_to_checkout(driver)

    # Fill out the checkout form
    fill_checkout_form(driver, "John", "Doe", "12345")

    # Verify order summary
    verify_order_summary(driver, product)

    # Verify finish process
    finish_checkout(driver)

    time.sleep(1)

    driver.quit()


if __name__ == "__main__":
    main()