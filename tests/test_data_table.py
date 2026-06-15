from pages.data_table_page import DataTablePage
from datetime import datetime

# Scenario: Verify all column headers in the data table


def test_verify_all_column_headers(page):

    data_table = DataTablePage(page)

    data_table.open()

    actual_headers = data_table.get_column_headers()

    expected_headers = [
        "Sr No.",
        "Book Name",
        "Book Genre",
        "Book Author",
        "Book ISBN",
        "Book Published",
    ]

    assert actual_headers == expected_headers
    print("Actual Headers:", actual_headers)


# Scenario: Verify the number of rows in the data table


def test_verify_number_of_rows(page):

    data_table = DataTablePage(page)

    data_table.open()

    rows = data_table.get_row_count()

    assert rows == 10


# Scenario: Verify the content of a specific cell in the data table


def test_verify_specific_cell_content(page):

    data_table = DataTablePage(page)

    data_table.open()

    book = data_table.get_book_name(2)

    print(book)

    assert len(book) > 0


# Scenario:Verify ISBN of a specific book in the data table


def test_verify_book_isbn(page):

    data_table = DataTablePage(page)

    data_table.open()

    isbn_numbers = data_table.get_all_isbn_numbers()

    for isbn in isbn_numbers:

        isbn = isbn.replace("-", "").replace(" ", "")

        assert len(isbn) in [10, 13]

        print("ISBN:", isbn)


# Scenario: Verify the published date format of a book in the data table


def test_verify_date_format(page):

    data_table = DataTablePage(page)

    data_table.open()

    dates = data_table.get_all_published_dates()

    for date in dates:

        datetime.strptime(date, "%Y-%m-%d")


# Scenario: Print all data from the data table


def test_print_table_data(page):

    data_table = DataTablePage(page)

    data_table.open()

    data_table.print_table_data()
