from pages.base_page import BasePage
from utils.logger import logger


class HomePage(BasePage):

    URL = "https://www.arasutechglobal.in/"

    # Locators
    NAV_COMPETITIONS = "a.nav-link[href='/competitions']"
    NAV_REGISTER = "a:has-text('Register')"
    REGISTER_NOW_BTN = "a:has-text('Register Now')"
    VIEW_COMPETITIONS_BTN = "a:has-text('View Competitions')"
    PAGE_HEADING = "text=Online Competitions for Kids"

    def __init__(self, page):
        super().__init__(page)

    # ------------------------------------
    # Open Home Page
    # ------------------------------------
    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_load_state("networkidle")
        logger.info("Opened Home Page")

    # ------------------------------------
    # Verify Home Page Loaded
    # ------------------------------------
    def verify_home_page(self):
        assert self.is_visible(self.PAGE_HEADING), "Home page heading not visible"
        logger.info("Home Page Verified")

    # ------------------------------------
    # Verify Page Title
    # ------------------------------------
    def verify_title(self):
        super().verify_title("Arasutech Competition")
        logger.info("Home Page Title Verified")

    # ------------------------------------
    # Verify Competitions Menu Visible
    # ------------------------------------
    def verify_competition_menu(self):
        assert self.is_visible(self.NAV_COMPETITIONS), "Competitions menu not visible"
        logger.info("Competitions Menu Verified")

    # ------------------------------------
    # Click Competitions Menu
    # ------------------------------------
    def click_competitions(self):
        self.click(self.NAV_COMPETITIONS)
        self.page.wait_for_load_state("networkidle")
        logger.info("Clicked Competitions Menu")

    # ------------------------------------
    # Verify Register Button Visible
    # ------------------------------------
    def verify_register_button(self):
        assert self.page.locator(
            self.NAV_REGISTER
        ).first.is_visible(), "Register button not visible"
        logger.info("Register Button Verified")

    # ------------------------------------
    # Click Register
    # ------------------------------------
    def click_register(self):
        self.page.locator(self.NAV_REGISTER).first.click()
        self.page.wait_for_load_state("networkidle")
        logger.info("Clicked Register Button")
