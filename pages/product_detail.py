class ProductDetailPage:
    def __init__(self, page):
        self.page = page

    def verify_product_details_visible(self):
        assert self.page.locator(".product-information").is_visible()

        assert self.page.locator("text=Category: Women > Tops").is_visible()
        #assert self.page.locator("text=Price").is_visible()
        assert self.page.locator("text=Availability").is_visible()
        assert self.page.locator("text=Condition").is_visible()
        assert self.page.locator("text=Brand:").is_visible()