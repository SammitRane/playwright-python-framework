from pages.login_page import LoginPage


def test_login(browserInstance):
    page = browserInstance
    login = LoginPage(page)

    login.open_login_page()
    login.login("rane.sammit@gmail.com", "Sammit@3")

    login.verify_logged_in()