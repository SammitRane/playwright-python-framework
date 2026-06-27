from pages.base_page import BasePage
from playwright.sync_api import expect



class LoginPage(BasePage):

    EMAIL = "input[data-qa='login-email']"
    PASSWORD = "input[data-qa='login-password']"
    LOGIN_BTN = "button[data-qa='login-button']"

    def open_login_page(self):
        self.goto("https://automationexercise.com/login")

    def login(self, email, password):
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def verify_logged_in(self):
        logout_link = self.page.locator("a[href='/logout']")
        expect(logout_link).to_be_visible()