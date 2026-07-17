import pytest

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.negative_excel_reader import get_negative_registration_data
from utils.logger import logger


@pytest.mark.parametrize(
    "name,grade,school,email,file,expected", get_negative_registration_data()
)
def test_registration_negative(page, name, grade, school, email, file, expected):

    logger.info(f"Executing Negative Test : {name}")

    home = HomePage(page)
    register = RegistrationPage(page)

    home.open()
    home.click_register()

    register.enter_name(name)
    register.enter_grade(str(grade))
    register.enter_school(school)
    register.enter_email(email)

    if file:
        register.upload_file(file)

    register.click_submit()

    print(f"Negative Test Executed : {name}")
