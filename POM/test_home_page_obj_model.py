import playwright


class HomePageObjModel:
    def __init__(self,page) -> None:
        self.page = page
        self.home_page = self.page.get_by_role("link", name="Home")
        self.email_text = self.page.get_by_text("Enter your email address to")

class DevelopmentPageObjModel():
    def __init__(self,page) -> None:
        self.page = page
        self.dev_page = page.get_by_role("link", name="Development", exact=True)

class LoginPageObjModel():
    def __init__(self,username,password,page) -> None:
        self.username = username
        self.password = password
        self.page = page

    def login_and_return_page(self) -> playwright.Page:
        self.page.get_by_test_id("handle-button").click()
        self.page.get_by_test_id("signUp.switchToSignUp").click()
        self.page.get_by_role("button", name="Log in with Email").click()
        self.page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
        self.page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill(self.username)
        self.page.get_by_role("textbox", name="Password").click()
        self.page.get_by_role("textbox", name="Password").fill(self.password)
        self.page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
        self.page.locator("body").press("Escape")
        return self.page
