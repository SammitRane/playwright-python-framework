from pages.login_page import LoginPage


def test_login(browserInstance):
    page = browserInstance
    login = LoginPage(page)

    login.open_login_page()
    login.login("existing_user@mail.com", "Test@123")

    assert login.is_logged_in()