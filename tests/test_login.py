import allure
from pages.login_page import LoginPage


@allure.epic("Authentication")
@allure.feature("Login")
@allure.story("Existing User Login")
@allure.title("Verify existing user can login successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(browserInstance):
    page = browserInstance
    login = LoginPage(page)

    email = "rane.sammit@gmail.com"
    password = "Sammit@3"  # ideally move to config/env later

    with allure.step("Open login page"):
        login.open_login_page()

    with allure.step("Enter login credentials"):
        login.enter_credentials(email, password)

    with allure.step("Submit login form"):
        login.submit_login()

    with allure.step("Verify user is logged in successfully"):
        login.verify_login_success()