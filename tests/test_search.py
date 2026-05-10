import pytest
from pages.product_page import ProductPage

@pytest.mark.smoke
def test_search_returns_results(base_page, benchmark):
    page = ProductPage(base_page)
    page.open()
    benchmark(page.search, "Top")
    name = page.get_first_product_name()
    assert name, "No product name found after search"


@pytest.mark.regression
def test_search_invalid_keyword(base_page):
    page = ProductPage(base_page)
    page.open()
    page.search("NonExistentProduct")
    assert not page.is_product_visible(page.FIRST_PRODUCT_NAME), "Unexpected product found for invalid search keyword"
