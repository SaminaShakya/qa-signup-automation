from playwright.sync_api import Page, expect
from pages.signup_page import SignupPage
from utils.email_otp import GmailOTPReader
import time
import random

def test_signup_flow(page: Page) -> None:
    TEST_EMAIL = "testingtask42@gmail.com"
    APP_PASSWORD = "nvat baqz zsiy exea"

    timestamp = int(time.time())
    email = f"testingtask42+test{timestamp}@gmail.com"

    print(f"Using email: {email}")

    page.goto("https://authorized-partner.vercel.app/")

    signup = SignupPage(page)

    signup.click_get_started_link()
    signup.check_terms_checkbox()
    signup.click_continue_button()

    signup.fill_personal_information(
        first_name="Samu",
        last_name="Shakya",
        email_address=email,
        phone_number=f"98{random.randint(10000000, 99999999)}",
        password="Kathmanduu1#",
        confirm_password="Kathmanduu1#"
    )

    signup.click_next_button()

    expect(page.locator("text=Verify Code")).to_be_visible(timeout=15000)
    print("Waiting for OTP...")

    time.sleep(5)

    otp_reader = GmailOTPReader(TEST_EMAIL, APP_PASSWORD)
    otp = otp_reader.get_otp(timeout=40)

    if not otp:
        raise Exception("OTP not received")

    signup.fill_otp(otp)
    signup.click_verify_code_button()

    expect(page.get_by_role("textbox", name="Name")).to_be_visible(timeout=15000)

    page.get_by_role("textbox", name="Name").fill("Fiber Education")
    page.get_by_role("textbox", name="Role in Agency").fill("Counselor")
    page.get_by_role("textbox", name="Email Address").fill("fiber@gmail.com")
    page.get_by_role("textbox", name="Website").fill("fiber.com")
    page.get_by_role("textbox", name="Address", exact=True).fill("Kathmandu")

    page.get_by_role("combobox").click()
    page.get_by_text("Nepal").click()

    page.get_by_role("button", name="Next").click()

    page.get_by_role("combobox", name="Years of Experience").click()
    page.get_by_role("option", name="2 years").click()

    page.get_by_role("spinbutton", name="Number of Students Recruited").fill("70")
    page.get_by_role("textbox", name="Focus Area").fill("Undergraduate and Postgraduate")
    page.get_by_role("spinbutton", name="Success Metrics").fill("72")

    page.get_by_text("Career Counseling").click()
    page.get_by_text("Admission Applications").click()
    page.get_by_text("Visa Processing").click()

    page.get_by_role("button", name="Next").click()

    page.get_by_role("textbox", name="Business Registration Number").fill("7941122454")

    page.get_by_role("combobox", name="Preferred Countries").click()
    page.get_by_text("Australia").click()
    page.get_by_text("Canada").click()
    page.get_by_text("New Zealand").click()

    page.get_by_text("Universities").click()

    page.locator(".flex.flex-col.items-center input[type='file']").first.set_input_files("Snapchat-1373928409.jpg")
    page.get_by_role("button", name="Submit").click()

    expect(page).to_have_url(
        "https://authorized-partner.vercel.app/admin/profile",
        timeout=20000
    )

    print("TEST COMPLETED SUCCESSFULLY")
    page.screenshot(path="final_result.png")