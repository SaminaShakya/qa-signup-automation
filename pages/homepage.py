from playwright.sync_api import Page

class Homepage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_link = page.get_by_role("link", name="Get Started")
        
        def is_signup_link_visible(self):
            return self.signup_link.is_visible()