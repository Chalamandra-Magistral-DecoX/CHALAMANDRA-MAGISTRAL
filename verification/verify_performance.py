from playwright.sync_api import sync_playwright
import time
import os

def verify_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Listen for console logs and errors
        page.on("console", lambda msg: print(f"Console: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))

        # Navigate to the page
        print("Navigating to http://localhost:8080/index.html")
        try:
            page.goto("http://localhost:8080/index.html")
        except Exception as e:
            print(f"Error navigating: {e}")
            browser.close()
            return

        # Wait for the canvas to be present
        print("Waiting for canvas...")
        try:
            page.wait_for_selector("#canvas-container canvas", timeout=10000)
            print("Canvas found.")
        except Exception as e:
            print(f"Error finding canvas: {e}")
            # Take screenshot of error state
            page.screenshot(path="verification/error_state.png")
            browser.close()
            return

        print("Waiting 3 seconds for initial settle...")
        time.sleep(3)

        # Take screenshot of initial state
        page.screenshot(path="verification/performance_initial.png")
        print("Initial screenshot taken.")

        # Click the transform button
        print("Clicking transform button...")
        try:
            # Try desktop button first
            if page.is_visible("#toggle-demo-desktop"):
                page.click("#toggle-demo-desktop")
                print("Desktop button clicked.")
            elif page.is_visible("#toggle-demo-mobile"):
                page.click("#toggle-demo-mobile")
                print("Mobile button clicked.")
            else:
                print("No toggle button found visible.")
        except Exception as e:
            print(f"Error clicking button: {e}")

        print("Waiting 5 seconds for transition...")
        time.sleep(5)

        # Take screenshot of final state
        page.screenshot(path="verification/performance_final.png")
        print("Final screenshot taken.")

        browser.close()
        print("Verification complete.")

if __name__ == "__main__":
    if not os.path.exists("verification"):
        os.makedirs("verification")
    verify_performance()
