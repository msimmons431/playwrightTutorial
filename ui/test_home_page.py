import re
import time

from playwright.sync_api import Playwright, expect, sync_playwright

from POM.test_home_page_obj_model import DevelopmentPageObjModel, HomePageObjModel


def test_dev_page_obj_model(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://automationpanda.com/")
    dev_page_obj = DevelopmentPageObjModel(page)
    expect(dev_page_obj.dev_page).to_be_visible()
    page.get_by_role("link", name="Development", exact=True).click()
    some_text = page.get_by_text("Software development is a").text_content()
    print(f"\n\nXXXX SOME TEXT {some_text}\n")
    softdevpat = re.compile(r".*(Software development is a)\s.*")
    sftmatch = re.match(softdevpat, some_text)
    print(f"\n\nGROUP 1 {sftmatch.group(1)}\n")
    sftrep = re.sub(softdevpat,"I like herping better", some_text)
    print(f"\n\nSUB {sftrep.strip()}\n")
    text = "Python is fun to learn"
    words = text.split()
    print(f"\n\nTYPE WORDS {type(words)}\n")
    joinwords = ":".join(words)
    print(f"\n\nJOIN {joinwords}\n")
    print(f"\n\nJOIN TYPE {type(joinwords)}\n")

def home_page_obj_model(playwright: Playwright):
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
