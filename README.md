# Dual Engine Automation Framework

A test automation framework that runs the same test suite on both **Selenium** and
**Playwright** via a single CLI flag. Built to demonstrate cross-engine design,
abstract page object architecture, and real performance benchmarking.

![CI](https://github.com/Manas-277/dual-engine-automation-framework/actions/workflows/ci.yml/badge.svg)

---

## What This Project Demonstrates

- A single test suite executing on two different automation engines
- Engine-agnostic Page Object Model using Python abstract base classes
- Performance benchmarking via `pytest-benchmark` with real timing data
- GitHub Actions CI running both engines in parallel on every push

---

## Architecture

```
BasePage (ABC)
├── SeleniumBasePage     → Wraps Selenium WebDriver API
└── PlaywrightBasePage   → Wraps Playwright Page API

Page Objects (LoginPage, ProductPage, CartPage)
└── Use composition — receive a BasePage instance, never import engine directly

Tests
└── Call page object methods — zero engine-specific code
```

Engine is selected at runtime:

```bash
pytest --engine=selenium
pytest --engine=playwright
```

---

## Project Structure

```
dual-engine-automation-framework/
├── pages/
│   ├── base_page.py        # Abstract base + engine implementations
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
├── tests/
│   ├── test_login.py
│   ├── test_search.py
│   └── test_cart.py
├── .github/workflows/
│   └── ci.yml
├── conftest.py
├── pytest.ini
├── config.py               # Not committed — credentials via env/secrets
└── requirements.txt
```

---

## Performance Results

Benchmarks captured via `pytest-benchmark` across 5 rounds per test.

| Test Case                   | Selenium (mean) | Playwright (mean) | Faster Engine  |
|-----------------------------|-----------------|-------------------|----------------|
| test_search_returns_results | ~1372ms         | ~605ms            | Playwright 2x  |
| test_invalid_login          | ~1577ms         | ~1715ms           | Selenium       |

---

## Test Coverage

| Test                          | Type       | Description                              |
|-------------------------------|------------|------------------------------------------|
| test_valid_login              | smoke      | Login with valid credentials             |
| test_invalid_login_shows_error| regression | Error message on wrong credentials       |
| test_login_with_empty_fields  | regression | Login blocked with empty inputs          |
| test_search_returns_results   | smoke      | Search returns matching products         |
| test_search_invalid_keyword   | regression | Search with no results handled correctly |
| test_add_product_to_cart      | smoke      | Product added to cart successfully       |
| test_remove_product_from_cart | regression | Cart empty after item deletion           |

---

## Run Locally

**Prerequisites:** Python 3.11+, Google Chrome installed

```bash
git clone https://github.com/Manas-277/dual-engine-automation-framework.git
cd dual-engine-automation-framework
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

Create `config.py` in the root:

```python
BASE_URL = "https://automationexercise.com"
VALID_USER   = {"email": "your_email", "password": "your_password"}
INVALID_USER = {"email": "fake@notexist.com", "password": "wrongpass"}
```

Run tests:

```bash
pytest --engine=playwright --html=reports/report_playwright.html -v
pytest --engine=selenium   --html=reports/report_selenium.html   -v
```

---

## CI Pipeline

Both engines run as parallel jobs on every push to `main`.  
Test reports and screenshots are uploaded as downloadable artifacts after each run.  
Credentials are stored as GitHub Actions secrets — never in source code.

---

## Tech Stack

Python 3.11 · pytest · Selenium 4 · Playwright · pytest-benchmark · pytest-html · GitHub Actions

---

## Target Application

[AutomationExercise.com](https://automationexercise.com) — a free, purpose-built
web app for automation practice with login, product search, and cart functionality.