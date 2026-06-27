class HomePage:
    def __init__(self, page):
        self.page = page

    def verify_home_visible(self):
        assert self.page.locator("text=Home").is_visible()

    def go_to_products(self):
        self.page.click("a[href='/products']")