class SignupPage:

    def __init__(self, page):
        self.page = page

    def open_login_page(self):
        self.page.goto("https://automationexercise.com/login")

    def enter_signup_details(self, name, email):
        self.page.locator("input[data-qa='signup-name']").fill(name)
        self.page.locator("input[data-qa='signup-email']").fill(email)
        self.page.locator("button[data-qa='signup-button']").click()

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
        return self.page.locator("h2[data-qa='account-created']").is_visible()