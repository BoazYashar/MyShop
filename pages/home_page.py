import allure
from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Search for product: {query}")
    def search_product(self, query):
        try:
            self.wait_and_fill("#search_query_top", query)
            self.click_element("button[name='submit_search']")
            expect(self.page.locator(".product_list .product-container")).to_be_visible(timeout=10000)
        except Exception:
            screenshot_path = "error_search.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Search failure", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Failed to search for product")

    @allure.step("Open first product from results")
    def open_first_product(self):
        try:
            self.page.click(".product_list .product-container .product-name")
            expect(self.page.locator("#product")).to_be_visible(timeout=10000)
        except Exception:
            screenshot_path = "error_open_product.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Open product failure", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Failed to open product page")

    @allure.step("Select white color")
    def select_color_white(self):
        try:
            self.click_element("#color_8")
        except Exception:
            screenshot_path = "error_color_select.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Color selection failure", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("White color not available")

    @allure.step("Add product to cart")
    def add_product_to_cart(self):
        try:
            self.click_element("button.exclusive")
            self.page.wait_for_selector("#layer_cart", timeout=10000)
        except Exception:
            screenshot_path = "error_add_to_cart.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Add to cart failure", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Failed to add product to cart")

    @allure.step("Verify product added popup")
    def assert_product_added(self):
        try:
            text = self.page.locator(".layer_cart_product h2").inner_text()
            assert "Product successfully added" in text, f"Unexpected message: {text}"
        except Exception:
            screenshot_path = "error_popup_assert.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Popup verification failure", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Product added confirmation not shown")

    @allure.step("Close cart popup")
    def close_cart_popup(self):
        try:
            self.click_element(".cross")
        except Exception:
            screenshot_path = "error_close_popup.png"
            self.page.screenshot(path=screenshot_path)
            allure.attach.file(screenshot_path, name="Popup close failure", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Failed to close popup")
