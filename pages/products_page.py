class ProductsPage:
    def __init__(self, page):
        self.page = page

    def verify_all_products_page(self):
        assert "/products" in self.page.url
        assert self.page.locator("text=All Products").is_visible()

    def verify_product_list_visible(self):
        assert self.page.locator(".features_items").is_visible()

    def open_first_product(self):
        self.page.locator(".choose a").first.click()