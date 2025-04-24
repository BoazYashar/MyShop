import allure
from playwright.sync_api import expect

from config.test_config import BROWSER_CONFIG
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Logging in with email: {email}")
    def login(self, email, password):
        self.wait_and_fill("#email", email)
        self.wait_and_fill("#passwd", password)
        self.click_element("#SubmitLogin")
        self.assert_in_url("my-account")

    @allure.step("Asserting login failure")
    def assert_login_failed(self):
        try:
            expect(self.page.locator("text=Authentication failed.")).to_be_visible(
                timeout=BROWSER_CONFIG["default_timeout"])
        except Exception:
            self.safe_assert(False, "Login error alert not displayed", "login_failed")
