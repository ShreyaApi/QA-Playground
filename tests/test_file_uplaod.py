from pages.file_upload_page import FileUploadPage

# Scenario : upload file


def test_upload_file(page):

    upload = FileUploadPage(page)

    upload.open()

    upload.upload_file("testdata/upload/sample.txt")

    uploaded_file = upload.get_uploaded_file_name()

    print(uploaded_file)

    assert "sample.txt" in uploaded_file


# Scenario: download file(Image)


def test_download_image(page):

    upload = FileUploadPage(page)

    upload.open()

    with page.expect_download() as download_info:
        upload.download_image()

    download = download_info.value

    print(download.suggested_filename)

    assert download.suggested_filename.endswith((".png", ".jpg", ".jpeg"))


# Scenario: download pdf


def test_download_pdf(page):

    upload = FileUploadPage(page)

    upload.open()

    with page.expect_download() as download_info:
        upload.download_pdf()

    download = download_info.value

    print(download.suggested_filename)

    assert download.suggested_filename.endswith(".pdf")


# Scenario: download Excel


def test_download_excel(page):

    upload = FileUploadPage(page)

    upload.open()

    with page.expect_download() as download_info:
        upload.download_excel()

    download = download_info.value

    print(download.suggested_filename)

    assert download.suggested_filename.endswith((".xls", ".xlsx"))


# Scenario: download word


def test_download_word(page):

    upload = FileUploadPage(page)

    upload.open()

    with page.expect_download() as download_info:
        upload.download_word()

    download = download_info.value

    print(download.suggested_filename)

    assert download.suggested_filename.endswith((".doc", ".docx"))
