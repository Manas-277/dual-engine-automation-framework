from abc import ABC, abstractmethod
from playwright.sync_api import expect
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):

    @abstractmethod
    def navigate(self, url: str): pass

    @abstractmethod
    def click(self, locator: str): pass

    @abstractmethod
    def click_first(self, locator: str): pass

    @abstractmethod
    def fill(self, locator: str, value: str): pass

    @abstractmethod
    def get_text(self, locator: str) -> str: pass

    @abstractmethod
    def get_first_text(self, locator: str) -> str: pass

    @abstractmethod
    def is_visible(self, locator: str) -> bool: pass

    @abstractmethod
    def hover(self, locator: str): pass

    @abstractmethod
    def wait_until_visible(self, locator: str, timeout: int = 5): pass

    @abstractmethod
    def force_click_first(self, locator: str): pass

class SeleniumBasePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def _find(self, locator: str):
        """Auto-detect XPath vs CSS selector."""
        if locator.startswith("//") or locator.startswith("(//"):
            return self.driver.find_element("xpath", locator)
        return self.driver.find_element("css selector", locator)

    def _find_all(self, locator: str):
        if locator.startswith("//") or locator.startswith("(//"):
            return self.driver.find_elements("xpath", locator)
        return self.driver.find_elements("css selector", locator)

    def navigate(self, url: str):
        self.driver.get(url)

    def click(self, locator: str):
        self._find(locator).click()

    def click_first(self, locator: str):
        self._find_all(locator)[0].click()

    def fill(self, locator: str, value: str):
        el = self._find(locator)
        el.clear()
        el.send_keys(value)

    def get_text(self, locator: str) -> str:
        return self._find(locator).text

    def get_first_text(self, locator: str) -> str:
        return self._find_all(locator)[0].text

    def is_visible(self, locator: str) -> bool:
        try:
            return self._find(locator).is_displayed()
        except:
            return False
    
    def hover(self, locator: str):
        element = self._find(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def wait_until_visible(self, locator: str, timeout: int = 5):
        by = "xpath" if locator.startswith("//") or locator.startswith("(//") else "css selector"
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
    
    def force_click_first(self, locator: str):
        element = self._find_all(locator)[0]
        self.driver.execute_script("arguments[0].click();", element)

class PlaywrightBasePage(BasePage):
    def __init__(self, page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def click_first(self, locator: str):
        self.page.locator(locator).first.click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def get_first_text(self, locator: str) -> str:
        return self.page.locator(locator).first.inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
    
    def hover(self, locator: str):
        self.page.locator(locator).first.hover()

    def wait_until_visible(self, locator: str, timeout: int = 5):
        expect(self.page.locator(locator)).to_be_visible(timeout=timeout * 1000)
    
    def force_click_first(self, locator: str):
        self.page.locator(locator).first.click(force=True)