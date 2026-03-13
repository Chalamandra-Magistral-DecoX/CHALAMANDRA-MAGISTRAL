import os
import subprocess
import time
from playwright.sync_api import sync_playwright

def verify_scroll_optimization():
    server = subprocess.Popen(["python3", "-m", "http.server", "8000"])
    time.sleep(2)  # Wait for server to start

    os.makedirs("/home/jules/verification", exist_ok=True)
    screenshot_path = "/home/jules/verification/scroll_optimization.png"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Ignore 404 for Vercel insights
            page.route("**/_vercel/insights/script.js", lambda route: route.abort())

            print("Navigating to index.html...")
            page.goto("http://localhost:8000/index.html", wait_until="networkidle")

            # Scroll down slowly to trigger intersection observer and progress bar
            print("Scrolling down to trigger animations...")
            for y in range(0, 3000, 100):
                page.evaluate(f"window.scrollTo(0, {y})")
                page.wait_for_timeout(50)

            page.wait_for_timeout(1000)

            print("Taking screenshot...")
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

            browser.close()

    finally:
        server.terminate()

if __name__ == "__main__":
    verify_scroll_optimization()
