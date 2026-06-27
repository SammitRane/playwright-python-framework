import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browserInstance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("browserInstance")

        if page:
            screenshot_name = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_name, full_page=True)