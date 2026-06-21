from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.get_started_link = page.get_by_role("link", name="Get Started")
        self.terms_checkbox = page.get_by_role(
            "checkbox", name="I agree to the Terms of"
        )
        self.continue_button = page.get_by_role("button", name="Continue")

        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")
        self.email_address_input = page.get_by_role("textbox", name="Email Address")
        self.phone_number_input = page.get_by_role("textbox", name="Phone Number")
        self.password_input = page.locator("input[name='password']")
        self.confirm_password_input = page.locator("input[name='confirmPassword']")

        self.next_button = page.get_by_role("button", name="Next")
        
        self.otp_input = page.get_by_role("textbox").first
        self.verify_code_button = page.get_by_role("button", name="Verify Code")

    def click_get_started_link(self):
        self.get_started_link.click()

    def check_terms_checkbox(self):
        self.terms_checkbox.check()

    def click_continue_button(self):
        self.continue_button.click()

    def fill_personal_information(
        self,
        first_name: str,
        last_name: str,
        email_address: str,
        phone_number: str,
        password: str,
        confirm_password: str,
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_address_input.fill(email_address)
        self.phone_number_input.fill(phone_number)
        self.password_input.fill(password)
        self.confirm_password_input.fill(confirm_password)

    def click_next_button(self):
        self.next_button.click()
        self.page.wait_for_load_state("networkidle")

    def fill_otp(self, otp: str):
        self.otp_input.wait_for(state="visible", timeout=10000)
        self.otp_input.fill(otp)

    def click_verify_code_button(self):
        self.verify_code_button.click()
        self.page.wait_for_load_state("networkidle")