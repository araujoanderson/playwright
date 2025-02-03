from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(page)
        assert products_page.get_title() == "Products"
        assert products_page.get_product_count() > 0

        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("invalid_user", "wrong_password")

        assert "Epic sadface" in login_page.get_error_message()

        browser.close()
