import re
from idlelib import browser

from playwright.sync_api import Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1.0)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.locator("body").press("Escape")
    #page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="Log in with Email")).to_be_hidden()
    page.get_by_role("link", name="Shop Women", exact=True).click()
    page.get_by_role("link", name="Shop Women Winter").click()
    page.get_by_role("link", name="Look Book").click()

    # ---------------------
    #context.close()
    #browser.close()


with sync_playwright() as playwright:
    run(playwright)
