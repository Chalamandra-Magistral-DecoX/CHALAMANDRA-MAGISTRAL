from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # Wait for canvas to be present
        page.wait_for_selector("#canvas-container")

        # Give it some time to initialize and render first frame
        time.sleep(2)

        # Screenshot Initial State (Chaos)
        page.screenshot(path="verification/screenshot_initial.png")
        print("Initial screenshot taken.")

        # Click the transform button (Desktop version)
        # Note: Depending on viewport size, it might be hidden.
        # But headless default is usually 1280x720 so desktop button should be visible.
        # Let's try to click the desktop button first.
        try:
            page.click("#toggle-demo-desktop", timeout=2000)
            print("Clicked desktop toggle button.")
        except:
            print("Desktop button not found/visible, trying mobile...")
            page.click("#toggle-demo-mobile")
            print("Clicked mobile toggle button.")

        # Wait for animation (2 seconds should be enough for transitionFactor to change significantly)
        time.sleep(3)

        # Screenshot Transformed State (Clarity)
        page.screenshot(path="verification/screenshot_transformed.png")
        print("Transformed screenshot taken.")

        # Click again to revert
        try:
            page.click("#toggle-demo-desktop", timeout=2000)
        except:
            page.click("#toggle-demo-mobile")

        time.sleep(3)

        # Screenshot Reverted State (Chaos)
        page.screenshot(path="verification/screenshot_reverted.png")
        print("Reverted screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
