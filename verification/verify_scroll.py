from playwright.sync_api import sync_playwright

def verify_scroll():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            print("Navigating to index.html...")
            page.goto("http://localhost:8080/index.html")
            page.wait_for_load_state("networkidle")

            # Initial state
            progress_bar = page.locator("#scroll-progress")
            initial_width = progress_bar.evaluate("el => el.style.width")
            print(f"Initial progress width: {initial_width}")

            # Scroll down
            print("Scrolling down...")
            page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
            page.wait_for_timeout(1000) # Wait for throttle and transition

            # Check progress bar
            mid_width = progress_bar.evaluate("el => el.style.width")
            print(f"Mid progress width: {mid_width}")

            if not mid_width or float(mid_width.replace('%', '')) <= 0:
                print("Error: Progress bar did not update.")
            else:
                print("Success: Progress bar updated.")

            # Check reveal elements
            reveals = page.locator(".reveal.active")
            count = reveals.count()
            print(f"Active reveal elements: {count}")

            if count == 0:
                 print("Error: No elements revealed.")
            else:
                 print(f"Success: {count} elements revealed.")

            page.screenshot(path="verification/scroll_test.png")
            print("Screenshot saved to verification/scroll_test.png")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_scroll()
