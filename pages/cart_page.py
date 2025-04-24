import allure
from playwright.sync_api import Page
from pages.base_page import BasePage

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Cart behavior")
class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_link = page.locator("a[title='View my shopping cart']")
        self.delete_button = page.locator(".cart_quantity_delete")

    @allure.step("Navigating to cart")
    def go_to_cart(self):
        self.click_element("a[title='View my shopping cart']")

    @allure.step("Removing item from cart")
    def remove_item(self):
        self.delete_button.click()
        self.page.wait_for_timeout(2000)
