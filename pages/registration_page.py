import allure
from pages.base_page import BasePage
from playwright.sync_api import expect
from config.test_config import BROWSER_CONFIG


class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Creating new account with email: {email}")
    def create_account(self, email):
        self.wait_and_fill("#email_create", email)
        self.click_element("#SubmitCreate")
        expect(self.page.locator("#account-creation_form")).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"]
)

    @allure.step("Filling registration form with user data")
    def fill_registration_form(self, user):
        self.wait_and_fill("#customer_firstname", user["first_name"])
        self.wait_and_fill("#customer_lastname", user["last_name"])
        self.wait_and_fill("#passwd", user["password"])
        self.click_element("#submitAccount")

    @allure.step("Filling address form for user")
    def fill_address_form(self, user):
        with allure.step("Clicking 'Add my first address' button"):
            self.page.locator("span", has_text="Add my first address").click()
        self.wait_and_fill("#address1", "123 Test Street")
        self.wait_and_fill("#city", "Testville")
        self.page.select_option("#id_state", label="Alabama")
        self.wait_and_fill("#postcode", "12345")
        self.wait_and_fill("#phone_mobile", "1234567890")
        self.click_element("#submitAddress")
