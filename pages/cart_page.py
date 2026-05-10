from pages.base_page import BasePage

class CartPage:
    URL = "https://automationexercise.com/view_cart"

    CART_ITEM           = "tr[id='product-1']"
    ITEM_NAME           = "tr[id='product-1'] h4 a"
    ITEM_QUANTITY       = "tr[id='product-1'] td.cart_quantity button"
    DELETE_BUTTON       = "a[class='cart_quantity_delete']"
    EMPTY_CART_MESSAGE  = "//b[contains(text(), 'Cart is empty!')]"
    PROCEED_TO_CHECKOUT = "//a[contains(text(), 'Proceed To Checkout')]"

    def __init__(self, base: BasePage):
        self.base = base
    
    def open(self):
        self.base.navigate(self.URL)
    
    def get_item_name(self):
        return self.base.get_first_text(self.ITEM_NAME)
    
    def get_item_quantity(self):
        return self.base.get_first_text(self.ITEM_QUANTITY)
    
    def delete_item(self):
        self.base.click_first(self.DELETE_BUTTON)
        self.base.wait_until_visible(self.EMPTY_CART_MESSAGE)
    
    def is_cart_empty(self):
        return self.base.is_visible(self.EMPTY_CART_MESSAGE)
    
    def proceed_to_checkout(self):
        self.base.click(self.PROCEED_TO_CHECKOUT)