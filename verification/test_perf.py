from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Ignore vercel insights script 404
        page.route("**/_vercel/insights/script.js", lambda route: route.fulfill(status=200, body=""))

        # Listen for console errors
        errors = []
        page.on("pageerror", lambda err: errors.append(err))

        # Go to local server
        page.goto("http://localhost:8000")

        # Wait for canvas to load
        page.wait_for_selector("#canvas-container canvas")

        # Scroll down to trigger intersection observer
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)

        # Click the toggle button
        toggle_btn = page.locator("#toggle-demo-desktop")
        if toggle_btn.is_visible():
            toggle_btn.click()
            page.wait_for_timeout(2000)

        # Take a screenshot
        page.screenshot(path="verification/perf_verify.png")

        browser.close()

        if errors:
            print("Errors found:", errors)
            return False

        print("Verification passed! No JS errors.")
        return True

if __name__ == "__main__":
    verify()
