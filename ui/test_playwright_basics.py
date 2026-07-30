# The class import Page has the fixture page. Add that import so the IDE
# can display the methods in page.xxx
from playwright.sync_api import Playwright, Page, expect, sync_playwright

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
    page.goto("https://rahulshettyacademy.com")






