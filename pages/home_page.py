import allure
from playwright.sync_api import expect, Page
from config.test_config import BROWSER_CONFIG
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Homepage interactions")
class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator("#search_query_top")
        self.search_button = page.locator("button[name='submit_search']")
        self.product_result = page.locator(".product_list .product-container")
        self.product_name = page.locator(".product_list .product-container .product-name")
        self.color_white = page.locator("#color_8")
        self.add_button = page.locator("button.exclusive")
        self.cart_layer = page.locator("#layer_cart")
        self.cart_popup_close = page.locator(".cross")
        self.success_text = page.locator(".layer_cart_product h2")

    @allure.step("Search for product: {query}")
    def search_product(self, query):
        self.search_input.fill(query)
        self.search_button.click()
        try:
            expect(self.product_result).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"])
        except Exception:
            self.safe_assert(False, "Search results not visible", "error_search")

    @allure.step("Open first product from results")
    def open_first_product(self):
        try:
            self.product_name.click()
            expect(self.page.locator("#product")).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"])
        except Exception:
            self.safe_assert(False, "Product page did not load", "error_open_product")

    @allure.step("Select white color")
    def select_color_white(self):
        try:
            self.color_white.click()
        except Exception:
            self.safe_assert(False, "White color not selectable", "error_color_select")

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        try:
            self.add_button.click()
            expect(self.cart_layer).to_be_visible(timeout=BROWSER_CONFIG["default_timeout"])
        except Exception:
            self.safe_assert(False, "Cart popup not shown", "error_add_to_cart")

    @allure.step("Verify product added popup")
    def assert_product_added(self):
        try:
            text = self.success_text.inner_text()
            self.safe_assert("Product successfully added" in text, "Success popup not shown", "error_popup_assert")
        except Exception:
            self.safe_assert(False, "Success popup missing", "error_popup_missing")

    @allure.step("Close cart popup")
    def close_cart_popup(self):
        try:
            self.cart_popup_close.click()
        except Exception:
            self.safe_assert(False, "Failed to close popup", "error_close_popup")
