import re
from playwright.sync_api import Page, expect
from pages.homepage import Homepage
from pages.signup_page import SignupPage

def test_example(page: Page) -> None:
    page.goto("https://authorized-partner.vercel.app/")
    page.get_by_role("textbox", name="Email").fill("aerisa@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Kathmanduu1#")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_role("link", name="Get Started").get_by_role("button")).to_be_visible()