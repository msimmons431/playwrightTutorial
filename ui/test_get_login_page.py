from playwright.sync_api import Playwright, expect, sync_playwright

from POM.test_home_page_obj_model import LoginPageObjModel
from POM.test_home_page_obj_model import LoginPageObjModel as LoginPageObj


async def test_get_login_page_obj(playwright: Playwright):
    username="symon.storozhenko@gmail.com"
    password="test123"
    browser = playwright.chromium.launch(headless=True)
    #browser = playwright.chromium.launch(headless=False, slow_mo=999)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1/")
    #login_page_obj = LoginPageObj(username,password,page)
    #login_page = login_page_obj.login_and_return_page()
    #page.get_by_test_id("handle-button").click()
    button = page.get_by_test_id("handle-button")
    await expect(button).to_be_visible(timeout=15000)
    await button.click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill(self.username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(self.password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.locator("body").press("Escape")
    login_page.goto("https://symonstorozhenko.wixsite.com/website-1/account/my-account")
    expect(login_page.get_by_role("heading",name="symon.storozhenko"))
