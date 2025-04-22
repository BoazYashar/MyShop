import pytest
from playwright.sync_api import sync_playwright
from config.test_config import BROWSER_CONFIG


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=BROWSER_CONFIG["headless"], slow_mo=800)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def config():
    return BROWSER_CONFIG
