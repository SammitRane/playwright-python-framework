class AccountPage:

    def __init__(self, page):
        self.page = page

    # ---------------------------
    # Validations
    # ---------------------------
    def is_account_created_visible(self):
        return self.page.locator("h2[data-qa='account-created']").is_visible()

    # ---------------------------
    # Actions after account creation
    # ---------------------------
    def click_continue(self):
        self.page.locator("a[data-qa='continue-button']").click()

    def logout(self):
        self.page.locator("a[href='/logout']").click()

    def delete_account(self):
        self.page.locator("a[href='/delete_account']").click()
        self.page.locator("button").click()  # confirmation (if appears)