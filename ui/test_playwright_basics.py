# The class import Page has the fixture page. Add that import so the IDE
# can display the methods in page.xxx
import re
import time

from playwright.sync_api import Page, Playwright, expect, sync_playwright


# FYI: (playwright) in the function is a playwright pytest fixture.
def test_playwrightBasics(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


# FYI: (page) in the function is a playwright pytest fixture.
# It will by default launch a chromium headless mode 1 single context page
# saving you a few steps as seen in the above test_playwrightBasics function.
def test_playwrightShortCut(page: Page ):
    journeypat = re.compile(r'.*Choose Your Learning (Journey).*')
    page.goto("https://rahulshettyacademy.com")
    page.get_by_role("navigation").get_by_role("link", name="Learning Paths").click()
    text = page.get_by_text("Choose Your Learning Journey").text_content()
    jrnymatch = re.match(journeypat,text)
    print(f"DEBUG: Journey match is {jrnymatch.group(1)}") if jrnymatch.group(1) else print("No Journey?")
    page.close()


def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    #page.get_by_label("Password:").fill("FOO____@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="terms").click()
    page.get_by_role("button", name="Sign In").click()
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(8)





