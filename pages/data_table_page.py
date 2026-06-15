class DataTablePage:

    URL = "https://qaplayground.com/practice/data-table"

    def __init__(self, page):

        self.page = page

        self.table = page.locator("table").first

        self.books_table = page.locator("table").nth(0)

    def open(self):

        self.page.goto(self.URL)

    def get_column_headers(self):

        return self.table.locator("thead th").all_text_contents()

    def get_row_count(self):

        return self.books_table.locator("tbody tr").count()

    def get_book_name(self, row_number):

        row = self.books_table.locator("tbody tr").nth(row_number - 1)

        return row.locator("td").nth(1).text_content().strip()

    def get_all_isbn_numbers(self):

        isbn_list = []

        rows = self.books_table.locator("tbody tr")

        for i in range(rows.count()):

            isbn = rows.nth(i).locator("td").nth(4).text_content().strip()

            isbn_list.append(isbn)

            return isbn_list

    def get_all_published_dates(self):

        dates = []

        rows = self.books_table.locator("tbody tr")

        for i in range(rows.count()):

            date = rows.nth(i).locator("td").nth(5).text_content().strip()

            dates.append(date)

        return dates

    def print_table_data(self):

        rows = self.books_table.locator("tbody tr")

        for i in range(rows.count()):

            data = rows.nth(i).locator("td").all_text_contents()

            print(data)
