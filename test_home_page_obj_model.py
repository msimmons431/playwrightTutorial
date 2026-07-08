class HomePageObjModel:
    def __init__(self,page) -> None:
        self.page = page
        self.home_page = self.page.get_by_role("link", name="Home")
        self.email_text = self.page.get_by_text("Enter your email address to")
