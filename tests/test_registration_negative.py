import pytest

from pages.home_page import HomePage
from pages.registration_page import RegisterPage

from utils.negative_excel_reader import get_negative_registration_data
from utils.logger import logger


@pytest.mark.parametrize(
    "name,grade,school,email,file,expected",
    get_negative_registration_data()
)
def test_registration_negative(page,
                               name,
                               grade,
                               school,
                               email,
                               file,
                               expected):

    home = HomePage(page)
    register = RegisterPage(page)

    logger.info(f"\n========== {expected} ==========\n")

    home.open()

    home.click_competitions()

    home.click_register()

    if name:
        register.enter_name(name)

    if grade:
        register.enter_grade(str(grade))

    if school:
        register.enter_school(school)

    if email:
        register.enter_email(email)

    if file:
        register.upload_file(file)

    register.click_submit()

    validation_map = {

        "Student Name Required": register.NAME,

        "Grade Required": register.GRADE,

        "School Required": register.SCHOOL,

        "Email Required": register.EMAIL,

        "File Required": register.FILE

    }

    if expected == "Invalid Email":

        message = register.get_validation_message(register.EMAIL)

        assert "@" in message

    else:

        locator = validation_map[expected]

        message = register.get_validation_message(locator)

        assert message == "Please fill out this field."

    logger.info(message)

    page.screenshot(
        path=f"screenshots/{expected}.png",
        full_page=True
    )

    print(f"\n✅ {expected} PASSED\n")