from pages.home_page import HomePage


def test_home_page(page):

    home = HomePage(page)

    print("\n========== HOME PAGE TEST STARTED ==========\n")

    # Open Website
    home.open()

    # Validate URL
    assert "arasutechglobal.in" in home.get_url()

    print("Current URL :", home.get_url())

    # Validate Title
    print("Page Title :", home.get_title())

    # Verify Logo
    home.verify_logo()
    print("Logo displayed successfully")

    # Click Home
    home.click_home()
    print("Home menu clicked")

    # Click About
    home.click_about()
    print("About menu clicked")

    # Click competition
    home.click_competitions()
    print("Competitions menu clicked")

    # Click Contact
    home.click_register()
    print("Register menu clicked")

    # Screenshot
    home.take_screenshot("home_page.png")

    print("\nScreenshot captured")

    print("\n========== TEST PASSED ==========\n")
