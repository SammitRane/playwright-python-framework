import allure
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail import ProductDetailPage


@allure.epic("View Product Details")
@allure.feature("Product View")
@allure.story("View Product Details")
@allure.title("Verify user can browse and view product details successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_detail_flow(browserInstance):

    page = browserInstance

    login = LoginPage(page)
    home = HomePage(page)
    products = ProductsPage(page)
    product_detail = ProductDetailPage(page)

    email = "rane.sammit@gmail.com"
    password = "Sammit@3"
   
    with allure.step("Open login page"):
        login.open_login_page()

    with allure.step("Enter login credentials"):
        login.enter_credentials(email, password)

    with allure.step("Submit login form"):
        login.submit_login()

    with allure.step("Verify home page is visible"):
        home.verify_home_visible()

    with allure.step("Navigate to products page"):
        home.go_to_products()

    with allure.step("Verify products page loaded"):
        products.verify_all_products_page()

    with allure.step("Verify product list is visible"):
        products.verify_product_list_visible()

    with allure.step("Open first product"):
        products.open_first_product()

    with allure.step("Verify product details page"):
        product_detail.verify_product_details_visible()