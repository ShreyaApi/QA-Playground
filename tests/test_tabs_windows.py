from pages.tabs_windows_page import TabsWindowsPage

# Scenario : open a link in new tab


def test_open_link_in_new_tab(page):

    tabs = TabsWindowsPage(page)

    tabs.open()

    with page.context.expect_page() as new_page_info:
        tabs.click_open_home_page()

    new_page = new_page_info.value
    new_page.wait_for_load_state()

    print("New Tab Title:", new_page.title())

    assert "QA Playground" in new_page.title()


# Scenario: Open Multiple windows


def test_open_multiple_windows(page):

    tabs = TabsWindowsPage(page)

    tabs.open()

    tabs.click_open_multiple_windows()

    page.wait_for_timeout(3000)

    pages = page.context.pages

    print("Total Windows:", len(pages))

    for p in pages:
        print("Title:", p.title())

    assert len(pages) > 1


# Scenario: switch back to parent window


def test_switch_back_to_parent_window(page):

    tabs = TabsWindowsPage(page)

    tabs.open()

    # Store parent page
    parent_page = page

    # Open child tab
    with page.context.expect_page() as child_page_info:
        tabs.click_open_home_page()

    child_page = child_page_info.value
    child_page.wait_for_load_state()

    # Read child title
    child_title = child_page.title()
    print("Child Title:", child_title)

    # Switch back to parent page
    parent_page.bring_to_front()

    # Verify parent title
    parent_title = parent_page.title()
    print("Parent Title:", parent_title)

    assert "Handle Multiple Windows and Tabs" in parent_title


# Scenario: Close child window and verify parent is active


def test_close_child_window(page):

    tabs = TabsWindowsPage(page)

    tabs.open()

    # Parent page reference
    parent_page = page

    # Open child tab
    with page.context.expect_page() as child_page_info:
        tabs.click_open_home_page()

    child_page = child_page_info.value
    child_page.wait_for_load_state()

    print("Total windows before close:", len(page.context.pages))

    # Close child tab
    child_page.close()

    # Switch back to parent
    parent_page.bring_to_front()

    print("Total windows after close:", len(page.context.pages))

    # Verify only parent window remains
    assert len(page.context.pages) == 1
