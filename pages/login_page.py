from pages.base_page import BasePage

class LoginPage:
    URL = "https://automationexercise.com/login"
    
    EMAIL_INPUT       = "input[data-qa='login-email']"
    PASSWORD_INPUT    = "input[data-qa='login-password']"
    LOGIN_BUTTON      = "button[data-qa='login-button']"
    ERROR_MESSAGE     = "//p[contains(text(), 'Your email or password is incorrect!')]"
    SUCCESS_INDICATOR = "(//ul[@class='nav navbar-nav']/li)[last()]"

    def __init__(self, base: BasePage):
        self.base = base
    
    def open(self):
        self.base.navigate(self.URL)
    
    def enter_email(self, email: str):
        self.base.fill(self.EMAIL_INPUT, email)
    
    def enter_password(self, password: str):
        self.base.fill(self.PASSWORD_INPUT, password)
    
    def submit(self):
        self.base.click(self.LOGIN_BUTTON)
    
    def login(self, email: str, password: str):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.submit()
    
    def is_login_successful(self):
        self.base.wait_until_visible(self.SUCCESS_INDICATOR)
        return "Logged in as" in self.base.get_text(self.SUCCESS_INDICATOR)
    
    def get_error_message(self):
        self.base.wait_until_visible(self.ERROR_MESSAGE)
        return self.base.get_text(self.ERROR_MESSAGE)