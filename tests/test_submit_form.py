from pages.forms_page import FormsPage
from utils.json_reader import read_json
from playwright.sync_api import expect


def test_submit_form(page):

    data = read_json("testdata/forms/form_data.json")

    user = data["valid_user"]

    form = FormsPage(page)

    form.open()

    form.fill_personal_details(
        user["first_name"], user["last_name"], user["email"], user["phone"], user["dob"]
    )

    form.select_gender()

    form.select_country(user["country"])

    form.enter_address(user["city"], user["about"])

    form.select_interests()

    form.enter_password(user["password"])

    form.accept_terms()

    form.click_submit()

    expect(form.success_message).to_have_text("Form Submitted Successfully!")
