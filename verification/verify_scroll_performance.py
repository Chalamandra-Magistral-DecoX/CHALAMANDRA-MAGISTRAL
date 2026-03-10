from playwright.sync_api import sync_playwright
import time

def verify_scroll_performance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Navigating to index.html...")
        page.goto("http://localhost:8000/index.html")
        page.wait_for_load_state("networkidle")

        # Check initial state
        print("Checking initial state...")
        progress_width = page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"Initial progress bar width: {progress_width}")

        # Verify first reveal section is NOT active immediately
        # Using a slight delay to allow observer to fire if it mistakenly triggers
        time.sleep(1)

        # Scroll down to trigger the first `.reveal` element
        print("Scrolling down to trigger reveal animations...")
        page.evaluate("window.scrollTo(0, 1500)")

        # Wait a moment for intersection observer and requestAnimationFrame to fire
        time.sleep(1)

        # Check new progress bar width
        new_progress_width = page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"New progress bar width: {new_progress_width}")

        if new_progress_width == "0%" or new_progress_width == progress_width:
            print("❌ Progress bar did not update correctly!")

        # Check if '.reveal' elements have '.active' class
        reveal_elements_active = page.evaluate('''() => {
            const reveals = document.querySelectorAll('.reveal');
            let activeCount = 0;
            for(let r of reveals) {
                if (r.classList.contains('active')) activeCount++;
            }
            return activeCount;
        }''')

        print(f"Found {reveal_elements_active} '.reveal' elements with '.active' class.")
        if reveal_elements_active == 0:
            print("❌ No reveal elements became active after scrolling!")
        else:
            print("✅ Intersection observer correctly triggered animations.")

        # Take a screenshot
        screenshot_path = "/home/jules/verification/scroll_test.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_scroll_performance()
