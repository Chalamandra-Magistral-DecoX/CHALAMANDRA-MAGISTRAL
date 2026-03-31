from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Capture console errors
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda exc: console_errors.append(str(exc)))

        print("Navigating to index.html...")
        try:
            page.goto("http://localhost:8080/index.html")
        except Exception as e:
            print(f"Navigation error: {e}")

        # Wait for initial load
        try:
            page.wait_for_load_state("networkidle", timeout=5000)
        except:
            print("Timed out waiting for network idle (expected due to 404s)")

        # Scroll down to trigger reveals
        print("Scrolling down...")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        time.sleep(1) # Wait for throttle and animation

        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

        # Check for revealed elements
        active_reveals = page.locator(".reveal.active").count()
        print(f"Found {active_reveals} active reveal elements.")

        # Take screenshot
        page.screenshot(path="verification/scroll_test.png", full_page=True)
        print("Screenshot saved to verification/scroll_test.png")

        # Filter out expected errors
        real_errors = [e for e in console_errors if "404" not in e and "Failed to load resource" not in e]

        if real_errors:
            print("REAL ERRORS FOUND:", real_errors)
            exit(1)
        else:
            print("No significant errors found.")

        browser.close()

if __name__ == "__main__":
    run()
