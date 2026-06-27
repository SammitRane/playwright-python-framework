from pages.base_page import BasePage


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

    def is_logged_in(self):
        return self.is_visible("a[href='/logout']")