import re, time
from playwright.sync_api import Playwright, expect, sync_playwright
from test_home_page_obj_model import HomePageObjModel

def test_home_page_obj_model(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=999)
    page = browser.new_page()
    page.goto("https://automationpanda.com/")
    home_page_obj = HomePageObjModel(page)
    expect(home_page_obj.home_page).to_be_visible()
    expect(home_page_obj.email_text).to_be_visible()
    emailpat = re.compile(".*\s(your email)\s.*")
    elem1 = page.get_by_text("Enter your email address").text_content()
    time.sleep(1)
    print(f"\n\nXXXX {elem1}\n")
    time.sleep(1)
    email_is_correct = emailpat.match(elem1)
    assert email_is_correct.group(1) == "your email"
    #expect(home_page_obj.email_text).to_be_visible()
