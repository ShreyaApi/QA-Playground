from pages import radio_checkbox_page
from playwright.sync_api import expect

# Scenario: Select Any One Radio Button


def test_select_radio_button(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    radio.select_yes_s1()

    assert radio.yes_radio_1.is_checked()

    radio.select_no_s1()

    assert radio.no_radio_1.is_checked()


# Scenario : only one radio button can be selected at a time


def test_only_one_radio_selected(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    radio.select_yes_s2()

    assert radio.yes_radio_2.is_checked()

    radio.select_no_s2()

    assert radio.no_radio_2.is_checked()

    assert not radio.yes_radio_2.is_checked()


# Scenario: Find the Bug


def test_find_bug(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    radio.select_yes_s3()

    assert radio.yes_radio_3.is_checked()

    radio.select_no_s3()

    assert radio.no_radio_3.is_checked()
    print("Yes Selected:", radio.yes_radio_3.is_checked())
    print("No Selected:", radio.no_radio_3.is_checked())


# Scenario:Find Which Radio Is Selected


def test_find_which_radio_selected(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    radio.select_bar()

    assert radio.is_bar_selected()

    assert not radio.is_foo_selected()


# Scenario: Verify if a radio button is enabled or disabled


def test_verify_radio_enabled_disabled(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    print("Going Enabled:", radio.is_going_enabled())
    print("Not Going Enabled:", radio.is_not_going_enabled())
    print("Maybe Enabled:", radio.is_maybe_enabled())

    assert radio.is_going_enabled()

    assert radio.is_not_going_enabled()

    assert not radio.is_maybe_enabled()


# Scenario: verify remember me checkbox is already checked or not


def test_verify_checkbox_checked(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    print("Remember Me Checked:", radio.remember_me_checkbox.is_checked())

    assert radio.remember_me_checkbox.is_checked()


# Scenario: Check the checkbox and verify if it's checked


def test_check_checkbox(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    radio.remember_me_checkbox.uncheck()

    radio.remember_me_checkbox.check()

    assert radio.remember_me_checkbox.is_checked()


# Scenario: Accept Terms & Conditions


def test_accept_terms_and_conditions(page):

    radio = radio_checkbox_page.RadioCheckboxPage(page)

    radio.open()

    radio.terms_checkbox.check()

    assert radio.terms_checkbox.is_checked()
