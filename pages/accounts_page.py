from playwright.sync_api import Page
import re


class AccountsPage:

    def __init__(self, page: Page):

        self.page = page

        self.account_balances = page.get_by_test_id("account-balance")

        self.account_rows = page.locator("tbody tr")

    def open(self):
        self.page.goto("https://qaplayground.com/bank/accounts")

    def get_account_count(self):
        return self.account_rows.count()

    def get_total_accounts_balance(self):

        total = 0

        count = self.account_balances.count()

        for i in range(count):

            text = self.account_balances.nth(i).text_content()

            print("Balance:", text)

            amount = re.search(r"\$\d{1,3}(?:,\d{3})*\.\d{2}", text)

            value = float(amount.group().replace("$", "").replace(",", ""))

            total += value

        print("Total:", total)

        return total
