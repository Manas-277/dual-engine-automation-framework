import pytest
from pages.login_page import LoginPage
from config import VALID_USER, INVALID_USER

@pytest.mark.smoke
def test_valid_login(base_page):
    page = LoginPage(base_page)
    page.login(VALID_USER["email"], VALID_USER["password"])
    assert page.is_login_successful()

@pytest.mark.regression
def test_invalid_login_shows_error(base_page, benchmark):
    page = LoginPage(base_page)
    benchmark(page.login, INVALID_USER["email"], INVALID_USER["password"])
    error = page.get_error_message()
    assert error, "Error message should be displayed for invalid login"

@pytest.mark.regression
def test_login_with_empty_field(base_page):
    page = LoginPage(base_page)
    page.login("","")
    assert not page.is_login_successful(), "Login should fail with empty credentials"
