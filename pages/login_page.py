from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_link = page.get_by_role("link", name="Login")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Log In")

    def click_login_link(self):
        self.login_link.click()

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()
