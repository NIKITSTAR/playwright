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

@pytest.fixture
def context(browser):
    """Создаёт новый контекст с записью видео. record_video_dir указывает, куда сохранять ролики."""
    context = browser.new_context(record_video_dir="allure-results")
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    # Закрываем страницу, чтобы видео гарантированно сохранилось
    page.close()

