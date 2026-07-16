import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        yield browser

        browser.close()


@pytest.fixture(scope="function")
def page(browser, request):

    context = browser.new_context()

    page = context.new_page()

    yield page

    # Take screenshot only if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        page.screenshot(
            path=f"screenshots/{request.node.name}.png",
            full_page=True
        )

    page.close()
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)