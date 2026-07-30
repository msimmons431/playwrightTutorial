import re

from playwright.sync_api import Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=900)
    context = browser.new_context()
    page = context.new_page()
    page.goto(
        "https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/"
    )
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="About", exact=True).click()
    with page.expect_popup() as page1_info:
        link_locator = page.get_by_role("link", name="A Python Orientation – How to")
        expect(link_locator).to_be_visible()
        page.get_by_role("link", name="A Python Orientation – How to").click()
    test_get_by_text = page.get_by_text("Enter your email address to")
    expect(test_get_by_text).to_be_visible()

    test_get_by_text_does_not_exist = page.get_by_text("ZAJLJLJLJSD")
    expect(test_get_by_text_does_not_exist).not_to_be_visible()
    page.get_by_text("Enter your email address to").click()
    link_locator = page.get_by_role("link", name="Home")
    expect(link_locator).to_be_visible()
    page1 = page1_info.value
    page1.close()
    page.locator("#menu-item-10593").get_by_role("link", name="Speaking").click()
    page.get_by_role("link", name="Teaching").click()
    page.get_by_role("link", name="BDD", exact=True).click()
    page.get_by_role("link", name="Development", exact=True).click()
    page.locator("#menu-item-6835").get_by_role("link", name="Testing").click()
    page.get_by_role("link", name="Software testing", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
