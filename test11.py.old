"""
This script tests adding a product to cart and compares titles and prices correspondence.
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


def main():
    # Initialize driver
    driver = Chrome()

    # Log in
    login.login(driver)

    # Locate product details
    print("Locating product details for the product...", end='')
    try:
        product_title = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]')
        product_add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
        product_description = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div')
        print('OK')
    except NoSuchElementException as e:
        print('Error')

    # Create a Product object and add it to cart
    product = Product(product_title, product_add_to_cart_button, product_price, product_description)
    print(f'Adding "{product.title_element.text}" product to cart')
    product.add_to_cart()
    
    # Locate cart button and its bage
    cart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    print('Locating cart button bage...', end='')
    try:
        cart_button_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        print('OK')
    except NoSuchElementException as e:
        print('Error')
        return

    # Go to cart
    print('Going into cart')
    cart_button.click()

    # Check cart's title and price
    print('Locating cart\'s content')
    try:
        cart_item_quantity = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[1]')
        cart_item_title = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
        cart_item_price = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
    except NoSuchElementException as e:
        print('Error')
        return
    print('Checking cart\'s item quantity, title and price...', end='')
    assert cart_item_quantity.text == '1', f"Expected 1 item in cart, but got {cart_item_quantity.text} instead"
    assert cart_item_title.text == product.name, f"Expected the product title in cart to be {product.name}, but got {cart_item_title.text} instead"
    assert cart_item_price.text == product.price, f"Expected the product price in cart to be {product.price}, but got {cart_item_price.text} instead"
    print('OK')
    
    # Close driver
    driver.quit()


if __name__ == "__main__":
    main()