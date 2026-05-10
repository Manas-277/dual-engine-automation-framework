from pages.base_page import BasePage

class ProductPage():
    URL = "https://automationexercise.com/products"

    SEARCH_INPUT        = "input[name='search']"
    SEARCH_BUTTON       = "button[id='submit_search']"
    PRODUCT_CARD        = "div[class='productinfo text-center']"
    FIRST_PRODUCT_NAME  = "div[class='productinfo text-center'] p"
    ADD_TO_CART_BUTTON  = "div[class='productinfo text-center'] a"
    CONTINUE_SHOPPING   = "//button[contains(text(), 'Continue Shopping')]"

    def __init__(self, base: BasePage):
        self.base = base
    
    def open(self):
        self.base.navigate(self.URL)
    
    def search(self, keyword: str):
        self.base.fill(self.SEARCH_INPUT, keyword)
        self.base.click(self.SEARCH_BUTTON)
    
    def get_first_product_name(self):
        return self.base.get_first_text(self.FIRST_PRODUCT_NAME)

    def add_first_product_to_cart(self):
        self.base.hover(self.PRODUCT_CARD)
        self.base.force_click_first(self.ADD_TO_CART_BUTTON)

    def dismiss_cart_modal(self):
        self.base.wait_until_visible(self.CONTINUE_SHOPPING)
        self.base.click(self.CONTINUE_SHOPPING)
    
    def is_product_visible(self, locator: str):
        return self.base.is_visible(locator)