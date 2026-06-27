class LoginPage:

    def __init__(self, page):
        self.page = page

    # ---------------------------
    # Navigation
    # ---------------------------
    def open_login_page(self):
        self.page.goto("https://automationexercise.com/login")

    # ---------------------------
    # Actions
    # ---------------------------
    def login(self, email, password):
        self.page.locator("input[data-qa='login-email']").fill(email)
        self.page.locator("input[data-qa='login-password']").fill(password)
        self.page.locator("button[data-qa='login-button']").click()

    # ---------------------------
    # Validations
    # ---------------------------
    def is_logged_in(self):
        return self.page.locator("a[href='/logout']").is_visible()

    def is_login_error_visible(self):
        return self.page.locator("p").filter(has_text="Your email or password is incorrect!").is_visible()