class DropdownPage:

    URL = "https://qaplayground.com/practice/dropdowns"

    def __init__(self, page):

        self.page = page

        # Scenario 1
        self.fruit_dropdown = page.locator("#dropdown-fruit")

        # Scenario 2
        self.country_dropdown = page.locator("#dropdown-country")

        # Scenario 3
        self.language_dropdown = page.locator("#dropdown-language")

        # Scenario 4
        self.superhero_dropdown = page.locator("#dropdown-heroes")

    def open(self):

        self.page.goto(self.URL)

    # Scenario 1

    def select_fruit(self, fruit):

        self.page.get_by_test_id("dropdown-fruit").click()

        self.page.get_by_role("option", name=fruit).click()

    def get_selected_fruit(self):

        return self.page.get_by_test_id("dropdown-fruit").text_content()

    # Scenario 2

    def select_country_by_value(self, value):

        self.page.get_by_test_id("dropdown-country").click()

        self.page.get_by_role("option", name="India").click()

    def get_country_value(self):

        return self.country_dropdown.text_content().strip()

    # Scenario 3

    def select_last_language(self):

        self.language_dropdown.click()

        options = self.page.get_by_role("option")

        count = options.count()

        last_option = options.nth(count - 1)

        language = last_option.text_content()

        last_option.click()

        return language

    def get_all_languages(self):

        self.language_dropdown.click()

        options = self.page.get_by_role("option")

        languages = options.all_text_contents()

        return languages

    # Scenario 4

    def select_multiple_heroes(self):

        self.superhero_dropdown.select_option(["ant-man", "batman", "avengers"])

    def get_selected_heroes(self):

        return self.superhero_dropdown.evaluate("""
            el => Array.from(el.selectedOptions)
            .map(option => option.value)
            """)
