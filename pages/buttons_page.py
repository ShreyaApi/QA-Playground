class ButtonsPage:

    URL = "https://qaplayground.com/practice/buttons"

    def __init__(self, page):
        self.page = page

        # Update these locators after inspecting the page
        self.single_click_btn = page.get_by_role("button", name="Go To Home")
        self.click_hold_btn = page.get_by_role("button", name="Click and Hold!")
        self.double_click_btn = page.get_by_role("button", name="Double Click Me")
        self.right_click_btn = page.get_by_role("button", name="Right Click Me")

    def open(self):
        self.page.goto(self.URL)

    def single_click(self):
        self.single_click_btn.click()

    def click_and_hold(self):

        self.click_hold_btn.hover()

        self.page.mouse.down()

        self.page.wait_for_timeout(1500)

        self.page.mouse.up()

    def double_click(self):
        self.double_click_btn.dblclick()

    def right_click(self):
        self.right_click_btn.click(button="right")

    def get_page_text(self):
        return self.page.locator("body").text_content()
