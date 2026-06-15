import re
from pages.dashboard_page import DashboardPage
from pages.accounts_page import AccountsPage


def test_dashboard_skeleton_loading(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    logged_in_page.wait_for_timeout(2000)

    # Verify dashboard container is visible
    assert dashboard.dashboard_container.is_visible()

    # Wait until loading is complete
    logged_in_page.wait_for_function("""
        () =>
        document
            .querySelector('#dashboard-page-container')
            .getAttribute('data-loading') === 'false'
        """)

    # Verify cards are visible
    assert dashboard.total_balance_card.is_visible()

    assert dashboard.accounts_count_card.is_visible()

    assert dashboard.transactions_count_card.is_visible()

    # Verify Total Balance contains $
    total_balance = dashboard.total_balance_card.text_content()

    amount = re.search(r"\$\d{1,3}(?:,\d{3})*\.\d{2}", total_balance)

    assert amount is not None

    print("Balance Amount:", amount.group())

    assert "$" in total_balance

    # Verify Accounts Count contains a number
    accounts_count = dashboard.accounts_count_card.text_content()

    count = re.search(r"\d+", accounts_count)

    assert count is not None

    print("Accounts Count:", count.group())

    assert any(char.isdigit() for char in accounts_count)

    # Verify Transactions Count contains a number
    transactions_count = dashboard.transactions_count_card.text_content()

    count = re.search(r"\d+", transactions_count)

    assert count is not None

    print("Transactions Count:", count.group())

    assert any(char.isdigit() for char in transactions_count)


# TC2: Stat card values match actual account and transaction data


def test_dashboard_values_match_accounts(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    logged_in_page.wait_for_timeout(4000)

    # Wait for dashboard load
    dashboard = DashboardPage(logged_in_page)

    assert dashboard.dashboard_container.is_visible()

    dashboard_balance = dashboard.get_total_balance()

    dashboard_accounts_count = dashboard.get_accounts_count()

    print("Dashboard Balance:", dashboard_balance)

    print("Dashboard Accounts:", dashboard_accounts_count)

    # Navigate to Accounts
    accounts = AccountsPage(logged_in_page)

    accounts.open()

    accounts_total = accounts.get_total_accounts_balance()

    accounts_count = accounts.get_account_count()

    print("Accounts Total:", accounts_total)

    print("Accounts Count:", accounts_count)

    # Validation
    assert dashboard_balance == accounts_total

    assert dashboard_accounts_count == accounts_count


# TC3: Quick Actions navigate to correct page


def test_quick_actions_navigation(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    # Dashboard loaded
    assert dashboard.dashboard_container.is_visible()

    # Add Account
    dashboard.click_add_account()

    assert "/bank/accounts" in logged_in_page.url

    assert dashboard.account_modal.is_visible()

    # Back to Dashboard
    logged_in_page.goto("https://qaplayground.com/bank/dashboard")

    # New Transaction
    dashboard.click_new_transaction()

    assert "/bank/transactions" in logged_in_page.url

    assert dashboard.transaction_modal.is_visible()


# TC4: Recent Transactions table shows up to 5 latest transactions


def test_recent_transactions_table(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    logged_in_page.wait_for_timeout(4000)

    # Verify table visible
    assert dashboard.recent_transactions_table.is_visible()

    # Verify rows count between 0 and 5
    rows_count = dashboard.get_transaction_rows_count()

    print("Rows Count:", rows_count)

    assert 0 <= rows_count <= 5

    # Validate each row
    for i in range(rows_count):

        row = dashboard.transaction_rows.nth(i)

        row_text = row.text_content()

        print(f"Row {i+1}:", row_text)

        # Type validation
        assert (
            "Deposit" in row_text or "Withdrawal" in row_text or "Transfer" in row_text
        )

        # Status validation
        assert "Completed" in row_text

        # Amount validation
        assert "$" in row_text


# TC5: Pinned Accounts section supports drag-and-drop reorder


def test_pinned_accounts_drag_drop(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    logged_in_page.wait_for_timeout(4000)

    # Verify section exists
    assert dashboard.pinned_accounts_section.is_visible()

    # Verify at least 2 cards exist
    count = dashboard.get_draggable_accounts_count()

    print("Draggable Accounts:", count)

    assert count >= 2

    # Verify draggable attribute
    for i in range(count):

        draggable = dashboard.draggable_accounts.nth(i).get_attribute("draggable")

        assert draggable == "true"

    # Capture initial order
    first_before = dashboard.get_account_name(0)

    second_before = dashboard.get_account_name(1)

    print("Before:")
    print(first_before)
    print(second_before)

    # Drag and Drop
    dashboard.drag_first_account_to_second()

    # Verify order changed
    first_after = dashboard.get_account_name(0)

    second_after = dashboard.get_account_name(1)

    print("After:")
    print(first_after)
    print(second_after)

    assert first_before != first_after or second_before != second_after

    # Reload page
    logged_in_page.reload()

    # Verify persistence
    assert dashboard.get_account_name(0) == first_after


# TC6: View all accounts


def test_view_all_accounts(logged_in_page):

    dashboard = DashboardPage(logged_in_page)

    dashboard.get_all_accounts()

    logged_in_page.wait_for_timeout(2000)

    assert "/bank/accounts" in logged_in_page.url

    assert logged_in_page.get_by_test_id("accounts-table").is_visible()
