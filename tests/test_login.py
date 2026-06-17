from pages.login_page import LoginPage
from utils.json_reader import read_json
from utils.logger import get_logger

# TC1 : Successful login with valid credentials


def test_valid_login(page):

    logger = get_logger()

    data = read_json("testdata/bank/login_data.json")

    login = LoginPage(page)

    logger.info("Opening Login Page")

    login.open()

    logger.info("Entering Credentials")

    login.login(data["admin_username"], data["admin_password"])

    page.wait_for_load_state()

    logger.info("Validating Dashboard")

    page.wait_for_timeout(2000)

    assert "dashboard" in page.url.lower()

    logger.info("Test Passed")


# TC2 : invalid Login


def test_invalid_login(page):

    data = read_json("testdata/bank/login_data.json")

    login = LoginPage(page)

    login.open()

    login.login(data["invalid_username"], data["invalid_password"])

    page.wait_for_load_state()

    error_message = login.get_error_message()
    assert "Invalid username or password" in error_message


# TC3: password visibility


def test_password_visibility(page):

    login = LoginPage(page)

    login.open()

    login.username.fill("admin")

    login.password.fill("admin123")

    # Hidden
    assert login.get_password_type() == "password"

    # Show
    login.toggle_password()

    assert login.get_password_type() == "text"

    # Hide again
    login.toggle_password()

    assert login.get_password_type() == "password"


# TC4: pressing Enter key in password field submits the login form


def test_login_using_enter(page):

    data = read_json("testdata/bank/login_data.json")

    login = LoginPage(page)

    login.open()

    login.press_enter_login(data["admin_username"], data["admin_password"])

    page.wait_for_load_state()

    page.wait_for_timeout(2000)

    assert "dashboard" in page.url.lower()


# TC5: Read-only viewer login grants restricted access


def test_viewer_login(page):

    data = read_json("testdata/bank/login_data.json")

    login = LoginPage(page)

    login.open()

    login.login(data["viewer_username"], data["viewer_password"])

    page.wait_for_load_state()

    page.wait_for_timeout(2000)

    assert "dashboard" in page.url.lower()
