import pytest

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.excel_reader import get_registration_data
from utils.logger import logger


@pytest.mark.parametrize("name,grade,school,email,file", get_registration_data())
def test_registration(page, name, grade, school, email, file):

    logger.info(f"\n========== Executing Registration Test : {name} ==========\n")

    home = HomePage(page)
    register = RegistrationPage(page)

    # Open Website
    home.open()

    # Verify Home Page
    home.verify_home_page()
    home.verify_title()

    # Navigate
    home.verify_competition_menu()
    home.click_competitions()

    home.verify_register_button()
    home.click_register()

    # Registration Page
    register.verify_registration_page()

    # Verify Fields
    register.verify_upload_field()
    register.verify_submit_button()

    # Fill Form
    register.enter_name(name)
    register.verify_name(name)

    register.enter_grade(str(grade))
    register.verify_grade(str(grade))

    register.enter_school(school)
    register.verify_school(school)

    register.enter_email(email)
    register.verify_email(email)

    register.upload_file(file)
    register.verify_uploaded_file(file)
    register.upload_file(file)

    register.verify_uploaded_file(file)

    register.verify_submit_button()

    # Screenshot
    register.take_screenshot(f"{name}.png")

    logger.info(f"Registration Completed Successfully : {name}")

    print(f"\n✅ {name} Registration Test PASSED\n")
