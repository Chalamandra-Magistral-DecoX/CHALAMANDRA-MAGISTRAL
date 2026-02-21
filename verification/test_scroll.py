
import os
import time
from playwright.sync_api import sync_playwright

def test_scroll_animations():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Initial state: Scroll progress should be 0%
        progress_width = page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"Initial progress width: {progress_width}")

        # Check first reveal element (header might be visible or not depending on layout)
        # But section#experiencia has .reveal and is further down.
        experiencia_section = page.locator("#experiencia")

        # It might not be active yet if it's below the fold
        # Let's check initial class
        initial_class = experiencia_section.get_attribute("class")
        print(f"Initial class for #experiencia: {initial_class}")

        # Scroll down
        print("Scrolling down...")
        page.evaluate("window.scrollTo(0, 1000)")
        time.sleep(1) # Wait for Observer to trigger and transition to start (though class add is immediate)

        # Check if active class is added
        after_scroll_class = experiencia_section.get_attribute("class")
        print(f"Class for #experiencia after scroll: {after_scroll_class}")

        if "active" in after_scroll_class:
            print("SUCCESS: 'active' class added to .reveal element.")
        else:
            print("FAILURE: 'active' class NOT added to .reveal element.")

        # Check progress bar
        new_progress_width = page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"New progress width: {new_progress_width}")

        if new_progress_width != "0%" and new_progress_width != "":
            print("SUCCESS: Progress bar updated.")
        else:
            print("FAILURE: Progress bar did not update.")

        browser.close()

if __name__ == "__main__":
    test_scroll_animations()
