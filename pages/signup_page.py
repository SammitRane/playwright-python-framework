from pages.base_page import BasePage


class SignupPage(BasePage):

    SIGNUP_NAME = "input[data-qa='signup-name']"
    SIGNUP_EMAIL = "input[data-qa='signup-email']"
    SIGNUP_BTN = "button[data-qa='signup-button']"

    def open_login_page(self):
        self.goto("https://automationexercise.com/login")

    def enter_signup_details(self, name, email):
        self.fill(self.SIGNUP_NAME, name)
        self.fill(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BTN)

    def fill_account_details(self):
        self.page.locator("#id_gender1").check()
        self.page.locator("#password").fill("Test@123")

        self.page.locator("#days").select_option("3")
        self.page.locator("#months").select_option("2")
        self.page.locator("#years").select_option("1995")

        self.page.locator("#first_name").fill("Sammit")
        self.page.locator("#last_name").fill("Rane")
        self.page.locator("#company").fill("Q Analytics")
        self.page.locator("#address1").fill("Kharegaon")
        self.page.locator("#address2").fill("Kalwa")

        self.page.locator("#country").select_option("India")
        self.page.locator("#state").fill("Maharashtra")
        self.page.locator("#city").fill("Thane")
        self.page.locator("#zipcode").fill("400605")
        self.page.locator("#mobile_number").fill("9876543210")

        self.page.locator("button[data-qa='create-account']").click()

    def is_account_created(self):
        return self.is_visible("h2[data-qa='account-created']")