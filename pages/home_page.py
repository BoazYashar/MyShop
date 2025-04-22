import allure
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("Searching for product: {query}")
    def search_product(self, query):
        self.wait_and_fill("#search_query_top", query)
        self.click_element("button[name='submit_search']")

    @allure.step("Opening first product from search results")
    def open_first_product(self):
        self.page.click(".product_list .product-container .product-name")

    @allure.step("Selecting color: White")
    def select_color_white(self):
        self.click_element("#color_8")  # white color swatch

    @allure.step("Adding product to cart")
    def add_product_to_cart(self):
        self.click_element("button.exclusive")  # Add to cart button on product page
        self.page.wait_for_selector("#layer_cart", timeout=10000)

    @allure.step("Closing cart popup")
    def close_cart_popup(self):
        self.click_element(".cross")