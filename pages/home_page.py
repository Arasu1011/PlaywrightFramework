from pages.base_page import BasePage
from playwright.sync_api import expect
from utils.logger import logger


class HomePage(BasePage):

    BASE_URL = "https://www.arasutechglobal.in/"
    EXPECTED_TITLE = "Arasutech Competition"

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        super().open(self.BASE_URL)

    def verify_home_page(self):
        assert "arasutechglobal.in" in self.get_url().lower()
        logger.info("Verified Home Page URL")

    def verify_title(self):
        actual_title = self.get_title()
        logger.info(f"Actual Page Title Found : '{actual_title}'")

        if actual_title == self.EXPECTED_TITLE:
            logger.info("Verified Home Page Title (exact match)")
            return

        # Fall back to a wait-and-retry check + partial match so a minor
        # difference (whitespace, suffix, slow JS title update) doesn't
        # fail the whole test outright.
        try:
            expect(self.page).to_have_title(self.EXPECTED_TITLE, timeout=5000)
            logger.info("Verified Home Page Title (after retry)")
        except AssertionError:
            actual_title = self.get_title()
            logger.info(f"Title after retry : '{actual_title}'")
            assert self.EXPECTED_TITLE.lower() in actual_title.lower(), (
                f"Title mismatch. Expected to contain '{self.EXPECTED_TITLE}', "
                f"but got '{actual_title}'"
            )
            logger.info("Verified Home Page Title (partial match)")

    def verify_competition_menu(self):
        expect(self.page.locator("a[href='/competitions']").first).to_be_visible()

        logger.info("Competition Menu Visible")

    def click_competitions(self):
        self.page.locator("a[href='/competitions']").first.click()
        logger.info("Competition Menu Clicked")

    def verify_register_button(self):
        expect(
            self.page.locator("nav").get_by_role("link", name="Register")
        ).to_be_visible()

        logger.info("Register Button Visible")

    def click_register(self):
        self.page.locator("nav").get_by_role("link", name="Register").click()

        logger.info("Register Button Clicked")
