import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """
        Создаёт и возвращает экземпляр браузера Chromium.

        Return: Экземпляр браузера Chromium.
        """
    playwright = sync_playwright().start()
    try:
        browser = playwright.chromium.launch(headless=False)
        yield browser
    finally:
        #Выполнится при любом исходе, в том числе если произошли исключения в тестах
        browser.close()
        playwright.stop()

@pytest.fixture
def context(browser):
    """
    Создаёт новый контекст браузера с записью видео.

    Args:
        browser: Экземпляр браузера, возвращаемый фикстурой browser.

    Return: Экземпляр контекста браузера с записью видео."""
    context = browser.new_context(record_video_dir="allure-results")
    yield context
    context.close()

@pytest.fixture
def page(context):
    """
        Создаёт новую страницу в рамках ранее созданного контекста.

        Args:
            context: Экземпляр контекста браузера, возвращаемый фикстурой context.

        Return: Экземпляр страницы браузера."""
    page = context.new_page()
    yield page
    # Закрываем страницу, чтобы видео гарантированно сохранилось
    page.close()

