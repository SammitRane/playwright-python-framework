import time
import allure
from pages.signup_page import SignupPage


@allure.epic("Authentication")
@allure.feature("Signup")
@allure.story("New User Registration")
@allure.title("Verify new user can create an account successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_signup(browserInstance):
    page = browserInstance
    signup = SignupPage(page)

    email = f"test_{int(time.time())}@mail.com"

    with allure.step("Open signup page"):
        signup.open_login_page()

    with allure.step("Enter user name and email"):
        signup.enter_signup_details("Sammit", email)

    with allure.step("Fill account registration form"):
        signup.fill_account_details()

    with allure.step("Submit form and verify account creation"):
        signup.verify_account_created()