from playwright.sync_api import expect


class ProductDetailPage:
    def __init__(self, page):
        self.page = page
        self.product_information = page.locator(".product-information")

    def verify_product_details_visible(self):
        # Verify product information section is visible
        expect(self.product_information).to_be_visible()

        # Verify product details
        expect(self.product_information).to_contain_text("Category")
        expect(self.product_information).to_contain_text("Availability")
        expect(self.product_information).to_contain_text("Condition")
        expect(self.product_information).to_contain_text("Brand")