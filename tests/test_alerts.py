from pages import alerts_page
from playwright.sync_api import expect

# Scenario: Handle a simple alert


def test_simple_alert(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alert_text = None

    def handle_dialog(dialog):
        nonlocal alert_text
        alert_text = dialog.message
        print(f"Alert Found: {alert_text}")
        page.wait_for_timeout(3000)

        dialog.accept()

    page.on("dialog", handle_dialog)

    alerts.click_simple_alert()

    assert alert_text == "Welcome to QA PlayGround!"


# Scenario: Handle a confirmation alert:Accept


def test_confirm_alert_accept(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alert_text = None

    def handle_dialog(dialog):
        nonlocal alert_text
        alert_text = dialog.message
        print(f"Alert Found: {alert_text}")
        page.wait_for_timeout(3000)

        dialog.accept()

    page.on("dialog", handle_dialog)

    alerts.click_confirm_alert()

    assert alert_text == "Do you know QA Playground?"


# Scenario: Handle a confirmation alert:Dismiss


def test_confirm_alert_dismiss(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alert_text = None

    def handle_dialog(dialog):
        nonlocal alert_text
        alert_text = dialog.message
        print(f"Alert Found: {alert_text}")
        page.wait_for_timeout(3000)

        dialog.dismiss()

    page.on("dialog", handle_dialog)

    alerts.click_confirm_alert()

    assert alert_text == "Do you know QA Playground?"


# Scenario: Handle a prompt alert


def test_prompt_alert(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alert_text = None

    def handle_dialog(dialog):
        nonlocal alert_text
        alert_text = dialog.message
        print(f"Alert Found: {alert_text}")
        page.wait_for_timeout(3000)

        dialog.accept("Shreya")

    page.on("dialog", handle_dialog)

    alerts.click_prompt_alert()

    assert alert_text == "Enter your name"


# Scenario: Handle a toast alert


def test_toast_alert(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alerts.click_toast_alert()

    toast_text = alerts.get_toast_message()

    assert toast_text == "This is simple toast."


# Scenario: Handle a sweet alert (you are!)


def test_sweet_alert(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alerts.click_sweet_alert()

    alerts.click_you_are()

    expect(page.get_by_role("heading", name="Modern Alert")).to_be_visible()


# Scenario: Handle a sweet alert (sometime)


def test_sweet_alert_sometime(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alerts.click_sweet_alert()

    alerts.click_sometime()


# Scenario: Handle share dialog


def test_share_dialog(page):

    alerts = alerts_page.AlertsPage(page)

    alerts.open()

    alerts.click_share()

    expect(alerts.share_link).to_be_visible()

    link = alerts.get_share_link()

    print("Share Link:", link)

    assert link == "https://www.qaplayground.com/practice/alerts-dialogs"

    alerts.copy_share_link()

    alerts.close_share_dialog()

    expect(alerts.share_link).not_to_be_visible()
