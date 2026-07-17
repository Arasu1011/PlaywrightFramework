import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False, slow_mo=300)

        yield browser

        browser.close()


@pytest.fixture(scope="function")
def page(browser, request):

    context = browser.new_context()

    page = context.new_page()

    yield page

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            os.makedirs("reports/screenshots", exist_ok=True)

            page.screenshot(
                path=f"reports/screenshots/{request.node.name}.png", full_page=True
            )

    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)
