from playwright.sync_api import Page


class FileUploadPage:

    def __init__(self, page: Page):
        self.page = page

        # Scenario 1 - Upload
        self.file_upload = page.locator("input[type='file']")

        # Scenario 2-5 - Download
        self.download_image_btn = page.get_by_role("button", name="Download Image")
        self.download_pdf_btn = page.get_by_role("button", name="Download PDF")
        self.download_excel_btn = page.get_by_role("button", name="Download Excel")
        self.download_word_btn = page.get_by_role("button", name="Download Word")

    def open(self):
        self.page.goto("https://qaplayground.com/practice/file-upload")

    # Upload
    def upload_file(self, file_path):
        self.file_upload.set_input_files(file_path)

    def get_uploaded_file_name(self):
        return self.file_upload.input_value()

    # Downloads
    def download_image(self):
        self.download_image_btn.click()

    def download_pdf(self):
        self.download_pdf_btn.click()

    def download_excel(self):
        self.download_excel_btn.click()

    def download_word(self):
        self.download_word_btn.click()
