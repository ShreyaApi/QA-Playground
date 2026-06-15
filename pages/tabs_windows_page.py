class TabsWindowsPage:

    URL = "https://qaplayground.com/practice/tabs-windows"

    def __init__(self, page):
        self.page = page

        self.open_home_page_btn = page.get_by_role("button", name="Open Home Page")

        self.open_multiple_windows_btn = page.get_by_test_id(
            "btn-open-multiple-windows"
        )

    def open(self):
        self.page.goto(self.URL)

    def click_open_home_page(self):
        self.open_home_page_btn.click()

    def click_open_multiple_windows(self):
        self.open_multiple_windows_btn.click()
