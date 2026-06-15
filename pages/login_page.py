from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.get_by_placeholder("Enter your username")
        self.password = page.get_by_placeholder("Enter your password")

        self.login_btn = page.get_by_test_id("login-button")
        self.clear_btn = page.get_by_test_id("clear-button")

        self.password_toggle = page.locator("#toggle-password")

        self.remember_me = page.get_by_label("Remember me")

        self.error_message = page.locator("#alert-message")

    def open(self):
        self.page.goto("https://qaplayground.com/bank")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

    def press_enter_login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.password.press("Enter")

    def toggle_password(self):
        self.password_toggle.click()

    def get_password_type(self):
        return self.password.get_attribute("type")

    def clear_form(self):
        self.clear_btn.click()

    def get_error_message(self):
        return self.error_message.text_content().strip()
