import allure
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    @allure.step("Filling input {selector} with value: {value}")
    def wait_and_fill(self, selector, value):
        expect(self.page.locator(selector)).to_be_visible(timeout=10000)
        self.page.fill(selector, value)

    @allure.step("Clicking element: {selector}")
    def click_element(self, selector):
        expect(self.page.locator(selector)).to_be_visible(timeout=10000)
        self.page.click(selector)

    @allure.step("Asserting current URL contains: {keyword}")
    def assert_in_url(self, keyword):
        assert keyword in self.page.url, f"Expected '{keyword}' in URL but got '{self.page.url}'"

    @allure.step("Waiting for element: {selector}")
    def wait_for_element(self, selector):
        expect(self.page.locator(selector)).to_be_visible(timeout=10000)

    @allure.step("Typing slowly into {selector}")
    def type_slowly(self, selector, text):
        self.page.click(selector)
        for char in text:
            self.page.keyboard.insert_text(char)
            self.page.wait_for_timeout(100)
