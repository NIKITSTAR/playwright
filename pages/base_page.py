from playwright.sync_api import Page, expect


class BasePage:
    """Базовый URL"""
    __BASE_URL: str = 'https://www.saucedemo.com'

    def __init__(self, page: Page) -> None:
        """Инициализирует объект BasePage. page: Экземпляр Playwright Page, с которым будет вестись работа."""
        self.page: Page = page
        self._endpoint: str = ''

    def _get_full_url(self) -> str:
        """Формирует и возвращает полный URL, объединяя базовый URL и endpoint. Возвращает полный URL в виде строки."""
        return f"{self.__BASE_URL}/{self._endpoint}"

    def navigate_to(self) -> None:
        """Переходит по сформированному URL и дожидается загрузки страницы. Также проверяет, что текущий URL совпадает с ожидаемым."""
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_click(self, selector: str) -> None:
        """Дожидается появления элемента по заданному селектору и кликает по нему. selector: CSS-селектор элемента."""
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_and_fill(self, selector: str, value: str) -> None:
        """Дожидается появления элемента по заданному селектору и заполняет его указанным значением. selector: CSS-селектор элемента. value: Текст для заполнения."""
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def wait_for_selector_and_type(self, selector: str, value: str, delay: float = 0.0) -> None:
        """Дожидается появления элемента по заданному селектору и вводит в него текст с заданной задержкой.
        selector: CSS-селектор элемента.
        value: Текст для ввода.
        delay: Задержка между нажатиями клавиш в миллисекундах."""
        self.page.wait_for_selector(selector)
        self.page.type(selector, value, delay=delay)

    def assert_element_is_visible(self, selector: str) -> None:
        """Проверяет, что элемент по заданному селектору виден на странице. selector: CSS-селектор элемента."""
        expect(self.page.locator(selector)).to_be_visible()

    def assert_text_present_on_page(self, text: str) -> None:
        """Проверяет, что на странице присутствует указанный текст. text: Текст, который ожидается на странице."""
        expect(self.page.locator("body")).to_contain_text(text)

    def assert_text_in_element(self, selector: str, text: str) -> None:
        """Проверяет, что элемент по заданному селектору содержит указанный текст. selector: CSS-селектор элемента. text: Текст, который ожидается в элементе."""
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_input_value(self, selector: str, expected_value: str) -> None:
        """Проверяет, что поле ввода по заданному селектору имеет указанное значение. selector: CSS-селектор поля ввода. expected_value: Ожидаемое значение в поле ввода."""
        expect(self.page.locator(selector)).to_have_value(expected_value)
