from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8000")

    # Check if page is loaded
    page.wait_for_selector("text=CAOS")

    # Test scrolling down slightly to trigger the scroll progress
    page.evaluate("window.scrollTo(0, 100)")

    # Wait a bit
    page.wait_for_timeout(1000)

    # Take screenshot to verify visual state
    page.screenshot(path="verification/test_result.png")

    print("Test passed successfully")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
