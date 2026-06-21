from playwright.sync_api import Page, expect
from pages.signup_page import SignupPage
from utils.email_otp import GmailOTPReader
import time

TEST_EMAIL = "medusatheterror@gmail.com"
APP_PASSWORD = "abcd efgh ijkl mnop"

def test_signup_auto_otp(page: Page) -> None:

    timestamp = int(time.time())
    email = f"medusatheterror+test{timestamp}@gmail.com"
    
    print(f"Signing up with: {email}")
    
    email_reader = GmailOTPReader(TEST_EMAIL, APP_PASSWORD)
    
    page.goto("https://authorized-partner.vercel.app/")
    signup_page = SignupPage(page)

    signup_page.click_get_started_link()
    signup_page.check_terms_checkbox()
    signup_page.click_continue_button()
    signup_page.fill_personal_information(
        first_name="Samu",
        last_name="Maharjan",
        email_address=email,
        phone_number="9825416754",
        password="Balance520#",
        confirm_password="Balance520#"
    )
    signup_page.click_next_button()
    
    expect(page.locator("text=Verify Code")).to_be_visible(timeout=10000)
    print("OTP page loaded - Waiting for OTP email...")
    
    otp = email_reader.get_otp(timeout=60)
    
    if otp:
        signup_page.fill_otp(otp)
        signup_page.click_verify_code_button()
        
        expect(page.get_by_role("textbox", name="Name")).to_be_visible(timeout=15000)
        print("OTP verified! Agency details page loaded.")
        page.screenshot(path="signup_auto_otp_success.png")
    else:
        raise Exception("Failed to get OTP from email")