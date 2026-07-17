from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    # -----------------------------
    # Browser
    # -----------------------------
    def open(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    # -----------------------------
    # Click
    # -----------------------------
    def click(self, locator):
        self.page.locator(locator).click()

    # -----------------------------
    # Enter Text
    # -----------------------------
    def type(self, locator, text):
        self.page.locator(locator).fill(text)

    # -----------------------------
    # Upload File
    # -----------------------------
    def upload(self, locator, filepath):
        self.page.locator(locator).set_input_files(filepath)

    # -----------------------------
    # Read Text
    # -----------------------------
    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    # -----------------------------
    # Visibility
    # -----------------------------
    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    # -----------------------------
    # Enabled
    # -----------------------------
    def is_enabled(self, locator):
        return self.page.locator(locator).is_enabled()

    # -----------------------------
    # Verify Text
    # -----------------------------
    def verify_text(self, locator, expected):
        actual = self.page.locator(locator).input_value()
        assert actual == expected

    # -----------------------------
    # Screenshot
    # -----------------------------
    def take_screenshot(self, filename):
        self.page.screenshot(path=f"reports/screenshots/{filename}", full_page=True)

    # -----------------------------
    # Title
    # -----------------------------
    def verify_title(self, expected):
        expect(self.page).to_have_title(expected)

    # -----------------------------
    # URL
    # -----------------------------
    def verify_url(self, expected):
        expect(self.page).to_have_url(expected)
