"""
This module contains reusable components for testing e-commerce functionality.
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import login


class Product:
    """Represents a product with add-to-cart functionality."""
    
    def __init__(self, title_element, add_to_cart_element, price_element, product_description):
        self.title_element = title_element
        self.name = title_element.text
        self.add_to_cart_element = add_to_cart_element
        self.price_element = price_element
        self.price = price_element.text
        self.description_element = product_description
        self.description = product_description.text

    def add_to_cart(self):
        """Clicks the 'Add to Cart' button for the product."""
        self.add_to_cart_element.click()


def setup_driver():
    """Initializes the WebDriver."""
    return Chrome()


def login_user(driver):
    """Logs in using the login module."""
    login.login(driver)


def add_product_to_cart(driver):
    """Adds a product to the cart and verifies cart details."""
    try:
        # Locate product details
        product_title = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]')
        product_add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
        product_description = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div')
    except NoSuchElementException as e:
        raise Exception("Product details could not be located.") from e

    # Create a Product object and add it to the cart
    product = Product(product_title, product_add_to_cart_button, product_price, product_description)
    product.add_to_cart()

    # Check cart button badge
    try:
        cart_button_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    except NoSuchElementException as e:
        raise Exception("Cart badge not found after adding product.") from e

    return product


def go_to_cart(driver):
    """Navigates to the cart page."""
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()


def verify_cart_contents(driver, product):
    """Verifies the cart contents."""
    try:
        cart_item_quantity = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[1]')
        cart_item_title = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
        cart_item_price = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
    except NoSuchElementException as e:
        raise Exception("Cart contents not found.") from e

    assert cart_item_quantity.text == '1', f"Expected 1 item in cart, but got {cart_item_quantity.text} instead"
    assert cart_item_title.text == product.name, f"Expected the product title in cart to be {product.name}, but got {cart_item_title.text} instead"
    assert cart_item_price.text == product.price, f"Expected the product price in cart to be {product.price}, but got {cart_item_price.text} instead"


def main():
    """Standalone usage for testing add-to-cart functionality."""
    driver = setup_driver()
    login_user(driver)
    product = add_product_to_cart(driver)
    go_to_cart(driver)
    verify_cart_contents(driver, product)
    time.sleep(1)
    driver.quit()


if __name__ == "__main__":
    main()