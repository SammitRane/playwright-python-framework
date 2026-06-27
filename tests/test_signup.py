import time
from pages.signup_page import SignupPage


def test_signup(browserInstance):
    page = browserInstance
    signup = SignupPage(page)

    email = f"test_{int(time.time())}@mail.com"

    signup.open_login_page()
    signup.enter_signup_details("Sammit", email)
    signup.fill_account_details()

    assert signup.is_account_created()