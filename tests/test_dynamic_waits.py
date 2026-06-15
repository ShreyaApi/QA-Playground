from pages.dynamic_waits_page import DynamicWaitsPage
from playwright.sync_api import expect

# Scenario: Handle Delayed Alert


def test_delayed_alert(page):

    dynamic = DynamicWaitsPage(page)

    dynamic.open()

    with page.expect_event("dialog") as dialog_info:
        dynamic.trigger_delayed_alert()

    dialog = dialog_info.value

    print("Alert Message:", dialog.message)

    page.wait_for_timeout(3000)

    assert "Appreciate you waiting!" in dialog.message

    dialog.accept()


# Scenario: Wait for hidden element to appear (3 seconds)


def test_hidden_element(page):

    dynamic = DynamicWaitsPage(page)

    dynamic.open()

    dynamic.show_element()

    message = page.get_by_text("Element is now visible!")

    expect(message).to_be_visible()

    assert message.text_content() == "Element is now visible!"


# Scenario: Wait for disabled button to be enabled (3 seconds)


def test_wait_for_button_enabled(page):

    dynamic = DynamicWaitsPage(page)

    dynamic.open()

    dynamic.activate_button()

    page.wait_for_timeout(3000)

    expect(dynamic.waiting_btn).to_be_enabled()

    print("Button became enabled and was clicked successfully")


# Scenario: Wait for text to change after loading data


def test_loading_text(page):

    dynamic = DynamicWaitsPage(page)

    dynamic.open()

    page.wait_for_timeout(5000)

    dynamic.load_data()

    expect(dynamic.status_text).to_have_text("Data Loaded!", timeout=5000)

    print("After:", dynamic.get_status_text())

    assert dynamic.get_status_text() == "Data Loaded!"


# Scenario: Wait for spinner to disappear after loading


def test_wait_for_spinner_to_disappear(page):

    dynamic = DynamicWaitsPage(page)

    dynamic.open()

    dynamic.start_spinner()

    # Wait for spinner to disappear
    expect(dynamic.spinner).to_be_hidden(timeout=3000)

    print("Status:", dynamic.get_spinner_status())

    assert dynamic.get_spinner_status() == "Done! Spinner gone."
