from pages.buttons_page import ButtonsPage

# Scenario: Single Click


def test_single_click(page):

    buttons_page = ButtonsPage(page)

    buttons_page.open()

    buttons_page.single_click()

    assert "QA PlayGround" in buttons_page.get_page_text()


# Scenario: Click and Hold


def test_click_and_hold(page):

    buttons_page = ButtonsPage(page)

    buttons_page.open()

    buttons_page.click_and_hold()

    assert "Hold Complete!" in buttons_page.get_page_text()


# Scenario: Double Click


def test_double_click(page):

    buttons_page = ButtonsPage(page)

    buttons_page.open()

    buttons_page.double_click()

    assert "Double" in buttons_page.get_page_text()


# Scenario: Right Click


def test_right_click(page):

    buttons_page = ButtonsPage(page)

    buttons_page.open()

    buttons_page.right_click()

    assert "Right" in buttons_page.get_page_text()
