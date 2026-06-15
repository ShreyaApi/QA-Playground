class DynamicWaitsPage:

    URL = "https://qaplayground.com/practice/dynamic-waits"

    def __init__(self, page):
        self.page = page

        # Scenario 1
        self.delayed_alert_btn = page.get_by_role(
            "button", name="Trigger Delayed Alert"
        )

        # Scenario 2
        self.show_element_btn = page.get_by_role("button", name="Show Element")

        # Scenario 3
        self.activate_btn = page.get_by_role("button", name="Activate Button")
        self.waiting_btn = page.get_by_test_id("btn-enable-after-delay")

        # Scenario 4
        self.load_data_btn = page.get_by_test_id("btn-load-data")
        self.status_text = page.get_by_test_id("load-status")

        # Scenario 5
        self.start_spinner_btn = page.get_by_role("button", name="Start Spinner")
        self.spinner = page.get_by_test_id("loading-spinner")
        self.spinner_status = page.get_by_test_id("spinner-done")

    def open(self):
        self.page.goto(self.URL)

    # Scenario 1
    def trigger_delayed_alert(self):
        self.delayed_alert_btn.click()

    # Scenario 2
    def show_element(self):
        self.show_element_btn.click()

    # Scenario 3
    def activate_button(self):
        self.activate_btn.click()

    # Scenario 4
    def load_data(self):
        self.load_data_btn.click()

    def get_status_text(self):
        return self.status_text.text_content().strip()

    # Scenario 5
    def start_spinner(self):
        self.start_spinner_btn.click()

    def get_spinner_status(self):
        return self.spinner_status.text_content().strip()
