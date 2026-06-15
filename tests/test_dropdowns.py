from pages.dropdown_page import DropdownPage

# Scenario 1: Select a fruit and verify the selection


def test_select_fruit(page):

    dropdown_page = DropdownPage(page)

    dropdown_page.open()

    dropdown_page.select_fruit("Apple")

    assert dropdown_page.get_selected_fruit() == "Apple"


# Scenario 2: Select a country by value and verify the selection


def test_select_country_by_value(page):

    dropdown_page = DropdownPage(page)

    dropdown_page.open()

    dropdown_page.select_country_by_value("In")

    assert dropdown_page.get_country_value() == "India"


# Scenario 3: Select the last language and verify the selection


def test_select_last_language(page):

    dropdown_page = DropdownPage(page)

    dropdown_page.open()

    selected_language = dropdown_page.select_last_language()

    languages = dropdown_page.get_all_languages()

    print("Languages:", languages)

    assert selected_language in languages


# Scenario 4: Select multiple superheroes and verify the selections


def test_select_multiple_heroes(page):

    dropdown_page = DropdownPage(page)

    dropdown_page.open()

    dropdown_page.select_multiple_heroes()

    selected_heroes = dropdown_page.get_selected_heroes()

    print("Selected Heroes:", selected_heroes)

    assert len(selected_heroes) == 3
