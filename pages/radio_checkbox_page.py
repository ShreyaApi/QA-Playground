class RadioCheckboxPage:

    URL = "https://qaplayground.com/practice/radio-checkbox"

    def __init__(self, page):
        self.page = page

        # Scenario 1
        self.yes_radio_1 = page.get_by_label("Yes").nth(0)
        self.no_radio_1 = page.get_by_label("No").nth(0)

        # Scenario 2
        self.yes_radio_2 = page.get_by_label("Yes").nth(1)
        self.no_radio_2 = page.get_by_label("No").nth(1)

        # Scenario 3
        self.yes_radio_3 = page.get_by_label("Yes").nth(2)
        self.no_radio_3 = page.get_by_label("No").nth(2)

        # Scenario 4
        self.foo_radio = page.get_by_test_id("radio-foo")
        self.bar_radio = page.get_by_test_id("radio-bar")

        # Scenario 5
        self.going_radio = page.get_by_test_id("radio-going")
        self.not_going_radio = page.get_by_test_id("radio-not-going")
        self.maybe_radio = page.get_by_test_id("radio-maybe")

        # Scenario 6

        self.remember_me_checkbox = page.get_by_label("Remember me")

        # Scenario 7
        self.terms_checkbox = page.get_by_label(
            "I agree to the FAKE terms and conditions"
        )

    def open(self):
        self.page.goto(self.URL)

    # Scenario 1
    def select_yes_s1(self):
        self.yes_radio_1.check()

    def select_no_s1(self):
        self.no_radio_1.check()

    # Scenario 2
    def select_yes_s2(self):
        self.yes_radio_2.check()

    def select_no_s2(self):
        self.no_radio_2.check()

    # Scenario 3
    def select_yes_s3(self):
        self.yes_radio_3.check()

    def select_no_s3(self):
        self.no_radio_3.check()

    # Scenario 4
    def select_foo(self):
        self.foo_radio.check()

    def select_bar(self):
        self.bar_radio.check()

    def is_foo_selected(self):
        return self.foo_radio.is_checked()

    def is_bar_selected(self):
        return self.bar_radio.is_checked()

    # Scenario 5
    def is_going_enabled(self):
        return self.going_radio.is_enabled()

    def is_not_going_enabled(self):
        return self.not_going_radio.is_enabled()

    def is_maybe_enabled(self):
        return self.maybe_radio.is_enabled()

    # Scenario 6
    def is_remember_me_checked(self):
        return self.remember_me_checkbox.is_checked()

    # Scenario 7
    def accept_terms(self):
        self.terms_checkbox.check()

    def is_terms_checked(self):
        return self.terms_checkbox.is_checked()
