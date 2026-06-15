class InputFieldsPage:

    URL = "https://qaplayground.com/practice/input-fields"

    def __init__(self, page):
        self.page = page

        self.movie_name = page.locator("#movieName")
        self.append_text = page.locator("#appendText")
        self.verify_text = page.locator("#insideText")
        self.clear_text = page.locator("#clearText")
        self.disabled_field = page.locator("#disabledInput")
        self.readonly_field = page.locator("#readonlyInput")

    def open(self):
        self.page.goto(self.URL)

    # Scenario 1
    def enter_movie_name(self, movie):
        self.movie_name.fill(movie)

    def get_movie_name(self):
        return self.movie_name.input_value()

    # Scenario 2
    def append_text_and_tab(self, text):
        self.append_text.click()
        self.append_text.press("End")
        self.append_text.press_sequentially(text)
        self.append_text.press("Tab")

    def get_append_text(self):
        return self.append_text.input_value()

    # Scenario 3
    def get_existing_text(self):
        return self.verify_text.input_value()

    # Scenario 4
    def clear_input_field(self):
        self.clear_text.clear()

    def get_cleared_text(self):
        return self.clear_text.input_value()

    # Scenario 5
    def is_disabled(self):
        return self.disabled_field.is_disabled()

    # Scenario 6
    def is_readonly(self):
        return self.readonly_field.get_attribute("readonly")
