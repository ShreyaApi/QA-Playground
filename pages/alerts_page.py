class AlertsPage:

    URL = "https://qaplayground.com/practice/alerts-dialogs"

    def __init__(self, page):

        self.page = page

        self.simple_alert_btn = page.get_by_role("button", name="Simple Alert")

        self.confirm_alert_btn = page.get_by_role("button", name="Confirm Alert")

        self.prompt_alert_btn = page.get_by_role("button", name="Prompt Alert")

        self.toast_alert_btn = page.get_by_role("button", name="Toast Alert")

        self.sweet_alert_btn = page.get_by_test_id("btn-modal-alert")

        self.sweet_alert_title = page.locator("#radix-_r_10s_")

        self.share_btn = page.get_by_role("button", name="Share")

        self.share_link = page.locator("input[readonly]")

        self.close_btn = page.get_by_test_id("btn-dialog-close")

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def click_simple_alert(self):
        self.simple_alert_btn.click()

    def click_confirm_alert(self):
        self.confirm_alert_btn.click()

    def click_prompt_alert(self):
        self.prompt_alert_btn.click()

    def click_toast_alert(self):
        self.toast_alert_btn.click()

    def click_sweet_alert(self):
        self.sweet_alert_btn.click()

    def click_you_are(self):
        self.page.get_by_test_id("btn-modal-confirm").click()

    def click_sometime(self):
        self.page.get_by_test_id("btn-modal-cancel").click()

    def click_share(self):
        self.share_btn.click()

    def get_share_link(self):
        return self.share_link.input_value()

    def copy_share_link(self):
        self.share_link.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Control+C")

    def close_share_dialog(self):
        self.close_btn.click()

    def get_toast_message(self):

        self.page.wait_for_timeout(2000)

        all_texts = self.page.locator("li").all_text_contents()

        for text in all_texts:
            if "toast" in text.lower():
                return text.strip()

        return None
