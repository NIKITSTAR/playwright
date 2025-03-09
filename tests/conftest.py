import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    try:
        browser = playwright.chromium.launch(headless=False)
        yield browser
    finally:
        """Выполнится при любом исходе, в том числе если произошли исключения в тестах"""
        browser.close()
        playwright.stop()
