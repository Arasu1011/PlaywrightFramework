from pages.base_page import BasePage
from utils.logger import logger


class RegisterPage(BasePage):

    # Locators
    NAME = "input[name='name']"
    GRADE = "input[name='grade']"
    SCHOOL = "input[name='school']"
    EMAIL = "input[name='email']"
    FILE = "input[type='file']"

    # Your button does NOT have type='submit'
    SUBMIT = "button.btn.btn-primary.w-100"

    def __init__(self, page):
        super().__init__(page)

    # --------------------------
    # Enter Student Name
    # --------------------------
    def enter_name(self, name):
        self.type(self.NAME, name)
        logger.info(f"Student Name : {name}")

    # --------------------------
    # Enter Grade
    # --------------------------
    def enter_grade(self, grade):
        self.type(self.GRADE, grade)
        logger.info(f"Grade : {grade}")

    # --------------------------
    # Enter School
    # --------------------------
    def enter_school(self, school):
        self.type(self.SCHOOL, school)
        logger.info(f"School : {school}")

    # --------------------------
    # Enter Email
    # --------------------------
    def enter_email(self, email):
        self.type(self.EMAIL, email)
        logger.info(f"Email : {email}")

    # --------------------------
    # Upload File
    # --------------------------
    def upload_file(self, filepath):
        self.upload(self.FILE, filepath)
        logger.info(f"Uploaded File : {filepath}")

    # --------------------------
    # Click Submit
    # --------------------------
    def click_submit(self):
        self.page.locator(self.SUBMIT).click()
        logger.info("Clicked Submit Button")

    # --------------------------
    # Verify Submit Button
    # --------------------------
    def is_submit_enabled(self):
        return self.page.locator(self.SUBMIT).is_enabled()

    # --------------------------
    # Verify Registration Page
    # --------------------------
    def verify_registration_page(self):
        return "register" in self.page.url.lower()
    # ---------------------------------------
    # ---------------------------------------
# Get Browser Validation Message
# ---------------------------------------
    def get_validation_message(self, locator):

        element = self.page.locator(locator)

        return element.evaluate(
          "el => el.validationMessage"
    )