import pytest
import allure
from utils.helpers import generate_random_email
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

@allure.feature("Full User Flow")
@allure.story("Registration → Login → Product → Cart")
@pytest.mark.smoke
def test_registration_login_cart_flow(page, config):
    base_url = config["base_url"]
    user = config["user"]
    email = generate_random_email(user["email_prefix"])

    with allure.step("Navigate to authentication page"):
        page.goto(f"{base_url}?controller=authentication&back=my-account")
        assert "authentication" in page.url

    with allure.step("Register new user"):
        reg_page = RegistrationPage(page)
        reg_page.create_account(email)
        reg_page.fill_registration_form(user)
        assert "controller=my-account" in page.url

    with allure.step("Logout after registration"):
        page.click(".logout")

    with allure.step("Login with newly created user"):
        login_page = LoginPage(page)
        login_page.login(email, user["password"])
        assert "controller=my-account" in page.url

    with allure.step("Search for product and add to cart with white color"):
        home_page = HomePage(page)
        home_page.search_product(config["search_query"])
        home_page.open_first_product()
        home_page.select_color_white()
        home_page.add_product_to_cart()
        home_page.close_cart_popup()

    with allure.step("Go to cart and remove item"):
        cart_page = CartPage(page)
        cart_page.go_to_cart()
        cart_page.remove_item()
