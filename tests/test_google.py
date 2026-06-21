import re  # re is for regular expression(used in title check)
from playwright.sync_api import (
    expect,
)  # imports expect library(expect gives smart test assertions like 'page should have this title")


def test_google_search(page):
    page.wait_for_timeout(3000)  # wait for 2 seconds
    page.goto("https://www.google.com/ncr")

    try:
        page.get_by_role("button", name="accept all").click(timeout=3000)
    except:
        print("no popup")

    page.get_by_role("combobox", name="Search").fill("Playwright Python")
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
    