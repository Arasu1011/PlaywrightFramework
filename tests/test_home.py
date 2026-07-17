from pages.home_page import HomePage


def test_home_page(page):

    home = HomePage(page)

    home.open()

    home.verify_home_page()

    home.verify_title()

    home.verify_competition_menu()

    home.verify_register_button()

    print("\nHome Page Test PASSED")
