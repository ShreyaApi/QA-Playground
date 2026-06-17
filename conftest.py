import pytest
import os

from pages.login_page import LoginPage
from utils.json_reader import read_json


@pytest.fixture(scope="function")
def page(browser, request):

    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("videos", exist_ok=True)

    context = browser.new_context(no_viewport=True, record_video_dir="videos/")

    page = context.new_page()

    page.set_default_timeout(60000)

    yield page

    # Runs AFTER test execution
    if request.node.rep_call.failed:

        page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)

    video_path = page.video.path()

    context.close()

    if request.node.rep_call.passed:

        if os.path.exists(video_path):
            os.remove(video_path)

        print("Passed video deleted")

    else:

        print(f"Failed video kept: {video_path}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def logged_in_page(page):

    data = read_json("testdata/bank/login_data.json")

    login = LoginPage(page)

    login.open()

    login.login(data["admin_username"], data["admin_password"])

    page.wait_for_load_state()

    return page
