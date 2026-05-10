import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playwright.sync_api import sync_playwright
from pages.base_page import SeleniumBasePage, PlaywrightBasePage
from pathlib import Path
Path("reports/screenshots").mkdir(parents=True, exist_ok=True)

def pytest_addoption(parser):
    parser.addoption(
        "--engine",
        action="store",
        default="playwright",
        help="Automation engine: selenium | playwright"
    )


@pytest.fixture(scope="session")
def engine(request):
    return request.config.getoption("--engine")

@pytest.fixture(scope="function")
def driver(engine, request):
    if engine == "selenium":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Chrome(options=options)
        yield drv
        drv.quit()
    elif engine == "playwright":
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            yield page
            page.screenshot(
                path=f"reports/screenshots/{request.node.name}.png",
                full_page=True
            )
            browser.close()
    
    else:
        raise ValueError(f"Unknown engine: {engine}. Use 'selenium' or 'playwright'.")

@pytest.fixture(scope="function")
def base_page(driver, engine):
    if engine == "selenium":
        return SeleniumBasePage(driver)
    elif engine == "playwright":
        return PlaywrightBasePage(driver)