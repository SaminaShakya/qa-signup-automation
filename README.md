# QA Signup Automation (Playwright + Pytest)

This project automates the end-to-end signup flow of the Authorized Partner platform, including OTP verification via Gmail and multi-step onboarding.

The framework is built using Playwright with Pytest and follows the Page Object Model (POM) design pattern.

---

## Features

- End-to-end automation of signup workflow
- Dynamic email and phone number generation
- OTP retrieval from Gmail using IMAP
- Multi-step onboarding automation
- File upload handling
- Final profile page verification
- Page Object Model (POM) structure

---

## Tech Stack

- Python 3.10+
- Playwright
- Pytest
- Gmail IMAP
- dotenv

---
## Setup Instructions

### 1. Clone Repository

git clone https://github.com/SaminaShakya/qa-signup-automation.git  
cd qa-signup-automation  

---

### 2. Create Virtual Environment

python -m venv venv  

Activate:

Windows  
venv\Scripts\activate  

Mac/Linux  
source venv/bin/activate  

---

### 3. Install Dependencies

pip install -r requirements.txt  

---

### 4. Install Playwright Browsers

playwright install  

---

### 5. Configure Environment Variables

Create a .env file in the project root:

GMAIL_APP_PASSWORD=your_app_password_here  

---

## Running Tests

### Run Test Suite

pytest tests/test_signup.py -v -s --headed  

### Generate HTML Report

pytest tests/test_signup.py --html=report.html --self-contained-html  

---

## Test Flow

1. Opens Authorized Partner signup page  
2. Accepts Terms and Conditions  
3. Fills personal details (name, email, phone, password)  
4. Submits signup form  
5. Waits for OTP verification screen  
6. Retrieves OTP from Gmail inbox  
7. Enters OTP and verifies account  
8. Fills agency details (name, role, email, website, address, country)  
9. Completes professional experience details  
10. Selects services and uploads document  
11. Submits final form  
12. Verifies successful navigation to profile page  

---

## Test Data Strategy

- Email: Dynamically generated using timestamp  
- Phone Number: Random 10-digit number starting with 98  
- Password: Static test password  
- Other fields: Fixed valid test data  

---

## Security Notes

- Gmail credentials are stored in .env
- .env file is excluded from version control
- No sensitive data is hardcoded in the codebase

---

## Known Limitations

- OTP delivery depends on Gmail response time
- IMAP must be enabled in Gmail account
- UI changes may require locator updates
- Requires stable internet connection

---

## Author

Samina Shakya  
QA Intern Candidate  

---

## Summary

This project demonstrates practical QA automation skills including:

- Playwright UI automation
- OTP-based authentication handling
- Multi-step form automation
- Page Object Model (POM)
- End-to-end signup workflow validation