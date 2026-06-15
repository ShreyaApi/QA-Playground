from pages import date_picker_page
from playwright.sync_api import expect
from datetime import datetime
from utils.json_reader import read_json

# Scenario : Enter today's date


def test_enter_today_date(page):

    date_picker = date_picker_page.DatePickerPage(page)

    date_picker.open()

    today = datetime.today().strftime("%Y-%m-%d")

    date_picker.enter_today_date(today)

    assert date_picker.get_today_date() == today


# Scenario: Enter birth date


def test_enter_birth_date(page):

    data = read_json("testdata/datepicker/birth_date.json")

    birth_date = data["birth_date"]

    date_picker = date_picker_page.DatePickerPage(page)

    date_picker.open()

    date_picker.enter_birth_date(birth_date)

    assert date_picker.get_birth_date() == birth_date


# Scenario: Enter a date range


def test_enter_date_range(page):

    data = read_json("testdata/datepicker/date_range.json")

    start_date = data["start_date"]
    end_date = data["end_date"]

    date_picker = date_picker_page.DatePickerPage(page)

    date_picker.open()

    date_picker.enter_start_date(start_date)
    date_picker.enter_end_date(end_date)

    assert date_picker.get_start_date() == start_date
    assert date_picker.get_end_date() == end_date


# Scenario: Date with min / max constraint


def test_enter_min_max_date(page):

    data = read_json("testdata/datepicker/min_max_date.json")

    min_date = data["min_date"]
    max_date = data["max_date"]

    date_picker = date_picker_page.DatePickerPage(page)

    date_picker.open()

    # Enter a valid date within the min/max range
    date_picker.enter_min_max_date(min_date)
    assert date_picker.get_min_max_date() == min_date

    # Attempt to enter an invalid date outside the min/max range
    date_picker.enter_min_max_date(max_date)
    assert date_picker.get_min_max_date() == max_date
