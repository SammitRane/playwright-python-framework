from pages.login_page import LoginPage


def test_login_valid(browserInstance):
    page = browserInstance
    login = LoginPage(page)

    login.open_login_page()
    login.login("rane.sammit@gmail.com", "Sammit@3")

    assert login.is_logged_in()