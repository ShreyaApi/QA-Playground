class LinksPage:

    URL = "https://qaplayground.com/practice/links"

    def __init__(self, page):

        self.page = page

        # Scenario 1
        self.home_link = page.get_by_test_id("link-internal-home")
        self.about_link = page.get_by_test_id("link-internal-about")

        # Scenario 2
        self.selenium_notes_link = page.get_by_test_id("link-external-selenium")

        self.selenium_course_link = page.get_by_test_id("link-external-course")

        # Scenario 3
        self.broken_new_tab_link = page.get_by_test_id("link-broken-newtab")

        self.broken_same_tab_link = page.get_by_test_id("link-broken-same")

        self.empty_href_link = page.get_by_test_id("link-broken-empty")

        # Scenario 4
        self.broken_image = page.get_by_alt_text("Broken image link")
        self.iron_man_image = page.get_by_alt_text("Iron Man")

        # Scenario 5
        self.broken_button = page.get_by_role("button", name="Broken Button")
        self.broken_link_button = page.get_by_role("button", name="Broken Link Button")
        self.home_button = page.get_by_role("button", name="Home Button")

        # Scenario 6
        self.link1 = page.get_by_role("link", name="Homdf56e")

    def open(self):
        self.page.goto(self.URL)

    # Scenario 1

    def click_home_link(self):
        self.home_link.click()

    def click_about_link(self):
        self.about_link.click()

    def get_home_href(self):
        return self.home_link.get_attribute("href")

    def get_about_href(self):
        return self.about_link.get_attribute("href")

    # Scenario 2

    def get_selenium_notes_target(self):
        return self.selenium_notes_link.get_attribute("target")

    def click_selenium_notes_link(self):
        self.selenium_notes_link.click()

    def click_selenium_course_link(self):
        self.selenium_course_link.click()

    def get_selenium_course_target(self):
        return self.selenium_course_link.get_attribute("target")

    def get_selenium_course_href(self):
        return self.selenium_course_link.get_attribute("href")

    # Scenario 3

    def get_broken_new_tab_href(self):
        return self.broken_new_tab_link.get_attribute("href")

    def get_broken_same_tab_href(self):
        return self.broken_same_tab_link.get_attribute("href")

    def get_empty_href(self):
        return self.empty_href_link.get_attribute("href")

    # Scenario 4
    def click_broken_image(self):
        self.broken_image.click()

    def click_iron_man_image(self):
        self.iron_man_image.click()

    # Scenario 5
    def click_broken_button(self):
        self.broken_button.click()

    def click_broken_link_button(self):
        self.broken_link_button.click()

    def click_home_button(self):
        self.home_button.click()
