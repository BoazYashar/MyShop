import allure
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