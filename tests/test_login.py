from playwright.sync_api import Page, expect
from pages.homepage import Homepage
from pages.login_page import LoginPage

def test_login(page: Page) -> None:
    page.goto("https://authorized-partner.vercel.app/")
    login_page = LoginPage(page)
    login_page.click_login_link()
    login_page.enter_email("aerisa@gmail.com")
    login_page.enter_password("Kathmanduu1#")
    login_page.click_login_button()

    homepage = Homepage(page)
    expect(homepage.signup_link).to_be_visible()
    homepage.click_performance()
    homepage.click_dashboard()