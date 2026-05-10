import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.smoke
def test_add_product_to_cart(base_page):
    product_page = ProductPage(base_page)
    product_page.open()
    product_page.add_first_product_to_cart()
    product_page.dismiss_cart_modal()

    cart_page = CartPage(base_page)
    cart_page.open()
    assert cart_page.get_item_name(), "No item name found in cart after adding product"

@pytest.mark.regression
def test_remove_product_from_cart(base_page):
    product_page = ProductPage(base_page)
    product_page.open()
    product_page.add_first_product_to_cart()
    product_page.dismiss_cart_modal()

    cart_page = CartPage(base_page)
    cart_page.open()
    cart_page.delete_item()
    assert cart_page.is_cart_empty(), "Cart should be empty after deleting the item"