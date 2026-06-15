from playwright.sync_api import Page
import re


class DashboardPage:

    def __init__(self, page: Page):

        self.page = page

        self.dashboard_container = page.locator("#dashboard-page-container")

        self.skeleton_cards = page.get_by_test_id("skeleton-card")

        self.total_balance_card = page.get_by_test_id("total-balance-card")

        self.accounts_count_card = page.get_by_test_id("accounts-count-card")

        self.transactions_count_card = page.get_by_test_id("transactions-count-card")

        self.account_button = page.get_by_test_id("nav-accounts")

        # Quick Actions
        self.quick_add_account = page.get_by_test_id("quick-add-account")
        self.quick_new_transaction = page.get_by_test_id("quick-new-transaction")

        # Modals
        self.account_modal = page.get_by_test_id("account-modal")
        self.transaction_modal = page.get_by_test_id("transaction-modal")

        # Recent Transactions Table
        self.recent_transactions_table = page.locator("#recent-transactions-section")

        self.transactions_tbody = page.get_by_test_id("transactions-tbody")

        # Pinned Accounts
        self.pinned_accounts_section = page.get_by_test_id("pinned-accounts-section")

        self.drop_zone = page.get_by_test_id("drop-zone")

        self.draggable_accounts = page.locator("[data-testid^='draggable-account-']")

        self.transaction_rows = self.transactions_tbody.locator("tr")

        # View all Accounts
        self.view_accounts_btn = page.get_by_test_id("quick-view-accounts")

    def get_loading_state(self):
        return self.dashboard_container.get_attribute("data-loading")

    def get_total_balance(self):

        text = self.total_balance_card.text_content()

        amount = re.search(r"\$\d{1,3}(?:,\d{3})*\.\d{2}", text)

        return float(amount.group().replace("$", "").replace(",", ""))

    def get_accounts_count(self):

        text = self.accounts_count_card.text_content()

        return int(re.search(r"\d+", text).group())

    def click_add_account(self):
        self.quick_add_account.click()

    def click_new_transaction(self):
        self.quick_new_transaction.click()

    def click_account_button(self):
        self.account_button.click()

    def get_transaction_rows_count(self):
        return self.transaction_rows.count()

    def get_draggable_accounts_count(self):
        return self.draggable_accounts.count()

    def get_account_name(self, index):
        return self.draggable_accounts.nth(index).text_content().strip()

    def drag_first_account_to_second(self):
        self.draggable_accounts.nth(0).drag_to(self.draggable_accounts.nth(1))

    def get_all_accounts(self):
        self.view_accounts_btn.click()
