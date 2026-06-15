class DatePickerPage:

    URL = "https://qaplayground.com/practice/date-picker"

    def __init__(self, page):
        self.page = page

        self.today_date = page.get_by_test_id("input-today-date")
        self.birth_date = page.get_by_test_id("input-birthday")

        self.start_date = page.get_by_test_id("input-date-start")
        self.end_date = page.get_by_test_id("input-date-end")

        self.min_max_date = page.get_by_test_id("input-date-restricted")

    def open(self):
        self.page.goto(self.URL)

    def enter_today_date(self, date):
        self.today_date.fill(date)

    def enter_birth_date(self, date):
        self.birth_date.fill(date)

    def enter_start_date(self, date):
        self.start_date.fill(date)

    def enter_end_date(self, date):
        self.end_date.fill(date)

    def enter_min_max_date(self, date):
        self.min_max_date.fill(date)

    def get_today_date(self):
        return self.today_date.input_value()

    def get_birth_date(self):
        return self.birth_date.input_value()

    def get_start_date(self):
        return self.start_date.input_value()

    def get_end_date(self):
        return self.end_date.input_value()

    def get_min_max_date(self):
        return self.min_max_date.input_value()
