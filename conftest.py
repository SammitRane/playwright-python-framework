from datetime import datetime
import os
import pytest

from playwright.sync_api import sync_playwright
from config.settings import SCREENSHOT_DIR


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

    # Capture screenshots only if the actual test fails
    if report.when == "call" and report.failed:

        # Get the Playwright page object from the fixture
        page = item.funcargs.get("browserInstance")

        # Skip screenshot for tests that don't use browserInstance
        if page:

            # Create screenshots directory if it doesn't exist
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)

            # Create unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = os.path.join(
                SCREENSHOT_DIR,
                f"{item.name}_{timestamp}.png"
            )

            # Capture screenshot
            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

