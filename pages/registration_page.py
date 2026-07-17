from pages.base_page import BasePage
from utils.logger import logger


class RegistrationPage(BasePage):

    # Application URL
    URL = "https://arasutechcontests.onrender.com"

    # Locators
    NAME = "input[name='name']"
    GRADE = "input[name='grade']"
    SCHOOL = "input[name='school']"
    EMAIL = "input[name='email']"
    FILE = "input[type='file']"
    SUBMIT = "button.btn.btn-primary.w-100"

    def __init__(self, page):
        super().__init__(page)

    # ------------------------------------
    # Open Registration Page
    # ------------------------------------
    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(5000)
        logger.info("Opened Registration Page")

    # ------------------------------------
    # Enter Student Name
    # ------------------------------------
    def enter_name(self, name):
        if name is not None:
            self.type(self.NAME, str(name))
            logger.info(f"Student Name : {name}")
        else:
            logger.info("Student Name left blank")

    # ------------------------------------
    # Enter Grade
    # ------------------------------------
    def enter_grade(self, grade):
        if grade is not None:
            self.type(self.GRADE, str(grade))
            logger.info(f"Grade : {grade}")
        else:
            logger.info("Grade left blank")

    # ------------------------------------
    # Enter School
    # ------------------------------------
    def enter_school(self, school):
        if school is not None:
            self.type(self.SCHOOL, str(school))
            logger.info(f"School : {school}")
        else:
            logger.info("School left blank")

    # ------------------------------------
    # Enter Email
    # ------------------------------------
    def enter_email(self, email):
        if email is not None:
            self.type(self.EMAIL, str(email))
            logger.info(f"Email : {email}")
        else:
            logger.info("Email left blank")

    # ------------------------------------
    # Upload File
    # ------------------------------------
    def upload_file(self, filepath):
        if filepath:
            self.upload(self.FILE, filepath)
            logger.info(f"Uploaded File : {filepath}")
        else:
            logger.info("No file uploaded")

    # ------------------------------------
    # Field Visibility Checks
    # ------------------------------------
    def verify_name(self, expected):
        if expected is not None:
            self.verify_text(self.NAME, expected)
            logger.info(f"Name Value Verified : {expected}")

    def verify_grade(self, expected):
        if expected is not None:
            self.verify_text(self.GRADE, str(expected))
            logger.info(f"Grade Value Verified : {expected}")

    def verify_school(self, expected):
        if expected is not None:
            self.verify_text(self.SCHOOL, expected)
            logger.info(f"School Value Verified : {expected}")

    def verify_email(self, expected):
        if expected is not None:
            self.verify_text(self.EMAIL, expected)
            logger.info(f"Email Value Verified : {expected}")

    def verify_upload_field(self):
        assert self.is_visible(self.FILE), "Upload field not visible"
        logger.info("Upload Field Verified")

    def verify_submit_button(self):
        assert self.is_visible(self.SUBMIT), "Submit button not visible"
        logger.info("Submit Button Verified")

    # ------------------------------------
    # Value Verifications (after entering)
    # ------------------------------------
    def verify_name(self, expected):
        self.verify_text(self.NAME, expected)
        logger.info(f"Name Value Verified : {expected}")

    def verify_grade(self, expected):
        self.verify_text(self.GRADE, expected)
        logger.info(f"Grade Value Verified : {expected}")

    def verify_school(self, expected):
        self.verify_text(self.SCHOOL, expected)
        logger.info(f"School Value Verified : {expected}")

    def verify_email(self, expected):
        self.verify_text(self.EMAIL, expected)
        logger.info(f"Email Value Verified : {expected}")

    # ------------------------------------
    # Verify File Was Uploaded
    # ------------------------------------
    def verify_uploaded_file(self, filepath):
        import os

        filename = os.path.basename(filepath)
        value = self.page.locator(self.FILE).input_value()
        assert (
            filename in value
        ), f"Expected '{filename}' in uploaded value, got '{value}'"
        logger.info(f"Uploaded File Verified : {filename}")

    # ------------------------------------
    # Click Submit
    # ------------------------------------
    def click_submit(self):
        self.click(self.SUBMIT)
        logger.info("Clicked Submit Button")

    # ------------------------------------
    # Verify Submit Button
    # ------------------------------------
    def is_submit_enabled(self):
        return self.is_enabled(self.SUBMIT)

    # ------------------------------------
    # Verify Registration Page
    # ------------------------------------
    def verify_registration_page(self):
        return "register" in self.page.url.lower()

    # ------------------------------------
    # Browser Validation Message
    # ------------------------------------
    def get_validation_message(self, locator):
        element = self.page.locator(locator)
        return element.evaluate("el => el.validationMessage")
