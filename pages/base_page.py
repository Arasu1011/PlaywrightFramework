from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    # Open URL
    def open(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    # Get Title
    def get_title(self):
        return self.page.title()

    # Get Current URL
    def get_url(self):
        return self.page.url

    # Click
    def click(self, locator):
        self.page.locator(locator).click()

    # Type Text
    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    # Upload File
    def upload(self, locator, filepath):
        self.page.locator(locator).set_input_files(filepath)

    # Screenshot
    def take_screenshot(self, filename):
        self.page.screenshot(path=f"screenshots/{filename}", full_page=True)

    # Wait
    def wait(self, seconds):
        self.page.wait_for_timeout(seconds * 1000)
