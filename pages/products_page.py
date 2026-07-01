import re

from playwright.sync_api import expect


class ProductsPage:

    def __init__(self, page):
        self.page = page

    def verify_all_products_page(self):
        expect(self.page).to_have_url(re.compile(r".*/products"))
        expect(self.page.get_by_text("All Products")).to_be_visible()

    def verify_product_list_visible(self):
        expect(self.page.locator(".features_items")).to_be_visible()

    def open_first_product(self):
        self.page.locator(".choose a").first.click()