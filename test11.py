"""
This script tests adding a product to the cart and compares titles and prices correspondence.
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import login


class Product:
    """Represents a product with title and add-to-cart functionality."""
    
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
    print("Locating product details for the product...")
    product_title = driver.find_element(By.ID, 'item_0_title_link')
    product_add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    product_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
    product_description = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div')

    # Create a Product object and add it to the cart
    product = Product(product_title, product_add_to_cart_button, product_price, product_description)
    print(f'Adding "{product.title_element.text}" product to the cart.')
    product.add_to_cart()

    # Print the product's info
    print(f'product: {product.name}')
    print(f'price: {product.price}')
    print(f'desc: {product.description}')

    # Pause for review (optional, for testing purposes)
    time.sleep(2)

    # Close driver
    driver.quit()


if __name__ == "__main__":
    main()