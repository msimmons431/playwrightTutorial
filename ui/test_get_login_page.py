from playwright.sync_api import Playwright, expect, sync_playwright

from POM.test_home_page_obj_model import LoginPageObjModel as LoginPageObj


def test_get_login_page_obj(playwright: Playwright):
    username="symon.storozhenko@gmail.com"
    password="test123"
    browser = playwright.chromium.launch(headless=False, slow_mo=999)
    page = browser.new_page()
    page.set_default_timeout(90000)
    page.goto("https://symonstorozhenko.wixsite.com/website-1/")
    login_page_obj = LoginPageObj(username,password,page)
    login_page = login_page_obj.login_and_return_page()
    login_page.goto("https://symonstorozhenko.wixsite.com/website-1/account/my-account")
    expect(login_page.get_by_role("heading",name="symon.storozhenko"))
