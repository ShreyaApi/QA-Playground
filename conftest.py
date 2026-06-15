import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.json_reader import read_json


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)

        # context = browser.new_context(viewport=None)

        page = browser.new_page()

        yield page

        browser.close()


@pytest.fixture
def logged_in_page(page):

    data = read_json("testdata/bank/login_data.json")

    login = LoginPage(page)

    login.open()

    login.login(data["admin_username"], data["admin_password"])

    page.wait_for_load_state()

    return page
