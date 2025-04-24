import pytest
import allure
from pages.login_page import LoginPage
from config.test_config import BROWSER_CONFIG


@allure.feature("Authentication")
@allure.story("Negative Login")
@pytest.mark.negative
def test_login_with_invalid_credentials(page):
    invalid_email = BROWSER_CONFIG["invalid_user"]["email"]
    invalid_password = BROWSER_CONFIG["invalid_user"]["password"]

    with allure.step("Navigate to login page"):
        page.goto(f"{BROWSER_CONFIG['base_url']}?controller=authentication&back=my-account")

    with allure.step("Attempt login with invalid credentials"):
        login_page = LoginPage(page)
        login_page.login(invalid_email, invalid_password)

    with allure.step("Verify login failed"):
        login_page.assert_login_failed()
