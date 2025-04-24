import allure
from playwright.sync_api import expect, Page
from config.test_config import BROWSER_CONFIG
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Login page behavior")
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#passwd")
        self.login_button = page.locator("#SubmitLogin")
        self.error_alert = page.locator("text=Authentication failed.")

    @allure.step("Logging in with email: {email}")
    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("Asserting login failure")
    def assert_login_failed(self):
        try:
            expect(self.error_alert).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"])
        except Exception:
            self.safe_assert(False, "Login error alert not displayed", "login_failed")
