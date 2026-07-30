from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    NokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    NokiaProduct.get_by_role("button").click()
    # expect is like an assertion
    expect(page.get_by_text("Checkout ( 2 ) (current)")).to_be_visible()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

