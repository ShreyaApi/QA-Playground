from pages.input_fields_page import InputFieldsPage

# Scenario: Fill the movie name input field


def test_movie_name_input(page):

    input_page = InputFieldsPage(page)

    input_page.open()

    input_page.movie_name.fill("Avengers")

    assert input_page.movie_name.input_value() == "Avengers"


# Scenario: Append text and press Tab


def test_append_text_and_press_tab(page):

    input_page = InputFieldsPage(page)

    input_page.open()

    input_page.append_text_and_tab(" Learning Playwright")

    assert "Learning Playwright" in input_page.get_append_text()


# Scenario: Verify text


def test_verify_existing_text(page):

    input_page = InputFieldsPage(page)

    input_page.open()

    assert input_page.get_existing_text() == "QA PlayGround"


# Scenario: Clear text


def test_clear_text(page):

    input_page = InputFieldsPage(page)

    input_page.open()

    input_page.clear_input_field()

    assert input_page.get_cleared_text() == ""


# Scenario: Check if the field is disabled


def test_verify_disabled_field(page):

    input_page = InputFieldsPage(page)

    input_page.open()

    assert input_page.is_disabled()


# Scenario: Check if the field is readonly


def test_verify_readonly_field(page):

    input_page = InputFieldsPage(page)

    input_page.open()

    assert input_page.is_readonly() is not None
