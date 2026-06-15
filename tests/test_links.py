from pages.links_page import LinksPage
import requests

# Scenario:Internal link


def test_verify_home_link(page):

    links = LinksPage(page)

    links.open()

    links.click_home_link()

    assert page.url == "https://qaplayground.com/"


def test_verify_about_link(page):

    links = LinksPage(page)

    links.open()

    links.click_about_link()

    assert page.url == "https://qaplayground.com/about-us"


# Scenario: External link


def test_verify_selenium_notes_link(page):

    links = LinksPage(page)

    links.open()

    # Verify target="_blank"
    assert links.get_selenium_notes_target() == "_blank"

    pages_before = len(page.context.pages)

    with page.context.expect_page() as new_page_info:
        links.click_selenium_notes_link()

    new_page = new_page_info.value

    # Verify new tab opened
    assert len(page.context.pages) == pages_before + 1

    # Verify switched to new tab
    assert new_page is not None


def test_verify_selenium_course_link(page):

    links = LinksPage(page)

    links.open()

    # Verify target="_blank"
    assert links.get_selenium_course_target() == "_blank"

    # Verify href exists
    href = links.get_selenium_course_href()
    assert href is not None

    pages_before = len(page.context.pages)

    # Click and capture new tab
    with page.context.expect_page() as new_page_info:
        links.click_selenium_course_link()

    new_page = new_page_info.value

    # Verify new tab opened
    assert len(page.context.pages) == pages_before + 1

    # Verify switched to new tab
    assert new_page is not None

    print("Course URL:", href)


# Scenario: Broken links opens in new tab


def test_broken_link_new_tab(page):

    links = LinksPage(page)
    links.open()

    href = links.get_broken_new_tab_href()

    # API Validation
    response = requests.get(href)

    print("Status Code:", response.status_code)

    assert response.status_code >= 400

    # UI Validation
    with page.context.expect_page() as new_page_info:
        links.broken_new_tab_link.click()

    page.wait_for_timeout(3000)

    new_page = new_page_info.value

    print("Opened URL:", new_page.url)


# Scenario: Broken links opens in same tab


def test_broken_link_same_tab(page):

    links = LinksPage(page)
    links.open()

    href = links.get_broken_same_tab_href()

    response = requests.get(href)

    print("Status Code:", response.status_code)

    assert response.status_code >= 400


# Scenario: Broken link with empty href


def test_broken_link_empty_href(page):

    links = LinksPage(page)
    links.open()

    href = links.get_empty_href()

    print("Href:", href)

    assert href in [None, "", "#"]


# Scenario: Broken image link same tab


def test_broken_image_link(page):

    links = LinksPage(page)
    links.open()

    links.click_broken_image()

    print("Navigated URL:", page.url)

    assert page.url == "https://qaplayground.com/practice/links"


# Scenario: Broken image link new tab


def test_broken_image_link_new_tab(page):

    links = LinksPage(page)
    links.open()

    with page.context.expect_page() as new_page_info:
        links.click_iron_man_image()

    new_page = new_page_info.value

    page.wait_for_timeout(6000)

    print("Opened URL:", new_page.url)
    assert new_page.url == "https://ashisheditz.com/?s=iron+man"
