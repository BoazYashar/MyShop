import allure
from playwright.sync_api import expect, Page
from config.test_config import BROWSER_CONFIG

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Registration page behavior")
class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_create_input = page.locator("#email_create")
        self.submit_create_button = page.locator("#SubmitCreate")
        self.account_form = page.locator("#account-creation_form")
        self.first_name_input = page.locator("#customer_firstname")
        self.last_name_input = page.locator("#customer_lastname")
        self.password_input = page.locator("#passwd")
        self.submit_account_button = page.locator("#submitAccount")
        self.add_address_button = page.locator("span:has-text('Add my first address')")
        self.address_input = page.locator("#address1")
        self.city_input = page.locator("#city")
        self.state_select = page.locator("#id_state")
        self.postcode_input = page.locator("#postcode")
        self.phone_input = page.locator("#phone_mobile")
        self.submit_address_button = page.locator("#submitAddress")

    @allure.step("Creating new account with email: {email}")
    def create_account(self, email):
        self.email_create_input.fill(email)
        self.submit_create_button.click()
        expect(self.account_form).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"])

    @allure.step("Filling registration form with user data")
    def fill_registration_form(self, user):
        self.first_name_input.fill(user["first_name"])
        self.last_name_input.fill(user["last_name"])
        self.password_input.fill(user["password"])
        self.submit_account_button.click()

    @allure.step("Filling address form for user")
    def fill_address_form(self, user):
        with allure.step("Clicking 'Add my first address' button"):
            self.add_address_button.click()
        self.address_input.fill("123 Test Street")
        self.city_input.fill("Testville")
        self.state_select.select_option(label="Alabama")
        self.postcode_input.fill("12345")
        self.phone_input.fill("1234567890")
        self.submit_address_button.click()
