class FormsPage:

    URL = "https://qaplayground.com/practice/forms"

    def __init__(self, page):
        self.page = page

        # Personal Details
        self.first_name = page.get_by_label("First Name")
        self.last_name = page.get_by_label("Last Name")
        self.email = page.get_by_test_id("input-email")
        self.phone = page.get_by_test_id("input-phone")
        self.dob = page.locator("#dob")

        # Gender
        self.male_radio = page.locator("#gender-male")
        self.female_radio = page.locator("#gender-female")
        self.other_radio = page.locator("#gender-other")

        # Address
        self.country_dropdown = page.locator("select")
        self.city = page.get_by_label("City")
        self.about_you = page.get_by_placeholder("Tell us a little about yourself...")

        # Interests
        self.selenium_checkbox = page.get_by_test_id("checkbox-interest-selenium")
        self.playwright_checkbox = page.get_by_test_id("checkbox-interest-playwright")
        self.cypress_checkbox = page.get_by_test_id("checkbox-interest-cypress")

        # Account Details
        self.password = page.get_by_placeholder("Min. 6 characters")
        self.confirm_password = page.get_by_placeholder("Re-enter password")

        self.terms_checkbox = page.get_by_label("I agree to the Terms & Conditions")

        self.submit_btn = page.locator("#submitFormBtn")

        self.reset_btn = page.locator("#resetFormBtn")

        self.success_message = page.locator("text=Form Submitted Successfully!")

    def open(self):
        self.page.goto(self.URL)

    def fill_personal_details(self, first_name, last_name, email, phone, dob):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.phone.fill(phone)
        self.dob.fill(dob)

    def select_gender(self):
        self.female_radio.check()

    def select_country(self, country):
        self.country_dropdown.select_option(label=country)

    def enter_address(self, city, about):
        self.city.fill(city)
        self.about_you.fill(about)

    def select_interests(self):
        self.selenium_checkbox.check()
        self.playwright_checkbox.check()
        self.cypress_checkbox.check()

    def enter_password(self, password):
        self.password.fill(password)
        self.confirm_password.fill(password)

    def accept_terms(self):
        self.terms_checkbox.check()

    def click_submit(self):
        self.submit_btn.click()

    def click_reset(self):
        self.reset_btn.click()

    def get_success_message(self):
        return self.success_message.text_content()
