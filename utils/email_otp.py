import imaplib
import email
import re
import time
from typing import Optional


class GmailOTPReader:
    def __init__(self, email_address: str, password: str):
        self.email = email_address
        self.password = password
        self.imap = None

    def connect(self):
        try:
            self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
            self.imap.login(self.email, self.password)
            self.imap.select("INBOX")
            print("Connected to Gmail.")
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def get_otp(self, timeout: int = 30) -> Optional[str]:
        if not self.connect():
            return None

        print(f"Waiting up to {timeout} seconds for OTP...")
        start = time.time()

        while time.time() - start < timeout:
            try:
                result, data = self.imap.search(
                    None,
                    '(SUBJECT "Signup Confirm OTP")'
                )

                if result != "OK" or not data[0]:
                    time.sleep(1)
                    print(".", end="", flush=True)
                    continue

                mail_ids = data[0].split()

                # Check newest emails first
                for mail_id in reversed(mail_ids[-10:]):
                    result, msg_data = self.imap.fetch(mail_id, "(RFC822)")

                    if result != "OK":
                        continue

                    msg = email.message_from_bytes(msg_data[0][1])

                    body = ""

                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(
                                    decode=True
                                ).decode(errors="ignore")
                                break
                    else:
                        body = msg.get_payload(
                            decode=True
                        ).decode(errors="ignore")

                    match = re.search(r"\b(\d{6})\b", body)

                    if match:
                        otp = match.group(1)

                        if otp != "000000":
                            print(f"\nOTP found: {otp}")
                            self.logout()
                            return otp

                time.sleep(1)
                print(".", end="", flush=True)

            except Exception as e:
                print(f"\nError: {e}")
                time.sleep(2)

        print("\nNo OTP found.")
        self.logout()
        return None

    def logout(self):
        if self.imap:
            try:
                self.imap.close()
            except:
                pass

            try:
                self.imap.logout()
            except:
                pass

            print("Disconnected.")