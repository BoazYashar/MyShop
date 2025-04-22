import allure
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Navigating to cart")
    def go_to_cart(self):
        self.click_element("a[title='View my shopping cart']")

    @allure.step("Removing item from cart")
    def remove_item(self):
        self.click_element(".cart_quantity_delete")
        self.page.wait_for_timeout(2000)
