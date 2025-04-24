import allure
from pages.base_page import BasePage
from playwright.sync_api import expect
from config.test_config import BROWSER_CONFIG


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Search for product: {query}")
    def search_product(self, query):
        self.wait_and_fill("#search_query_top", query)
        self.click_element("button[name='submit_search']")
        try:
            expect(self.page.locator(".product_list .product-container")).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"]
)
        except Exception:
            self.safe_assert(False, "Failed to find search results", "error_search")

    @allure.step("Open first product from results")
    def open_first_product(self):
        try:
            self.page.click(".product_list .product-container .product-name")
            expect(self.page.locator("#product")).to_be_visible(timeout=10000)
        except Exception:
            self.safe_assert(False, "Failed to open product page", "error_open_product")

    @allure.step("Select white color")
    def select_color_white(self):
        try:
            self.click_element("#color_8")
        except Exception:
            self.safe_assert(False, "White color not available", "error_color_select")

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        try:
            self.click_element("button.exclusive")
            self.page.wait_for_selector("#layer_cart", timeout=10000)
        except Exception:
            self.safe_assert(False, "Failed to add product to cart", "error_add_to_cart")

    @allure.step("Verify product added popup")
    def assert_product_added(self):
        try:
            text = self.page.locator(".layer_cart_product h2").inner_text()
            self.safe_assert("Product successfully added" in text, "Product added confirmation not shown",
                             "error_popup_assert")
        except Exception:
            self.safe_assert(False, "Product popup did not appear", "error_popup_missing")

    @allure.step("Close cart popup")
    def close_cart_popup(self):
        try:
            self.click_element(".cross")
        except Exception:
            self.safe_assert(False, "Failed to close popup", "error_close_popup")

    @allure.step("Verify login success")
    def assert_login_successful(self):
        try:
            expect(self.page.locator(".account")).to_be_visible(timeout=10000)
            self.safe_assert("controller=my-account" in self.page.url, "Login did not redirect to account page",
                             "error_login_url")
        except Exception:
            self.safe_assert(False, "Login failed or account page not loaded", "error_login")
