from playwright.sync_api import sync_playwright

def test_scroll_animations():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8000/index.html')

        # Check initial state
        progress_width = page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"Initial progress width: {progress_width}")

        # Scroll down
        page.evaluate("window.scrollBy(0, window.innerHeight)")
        page.wait_for_timeout(500)

        # Check progress bar updated
        progress_width = page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"Progress width after scroll: {progress_width}")

        # Check if reveal animations triggered
        active_reveals = page.evaluate("document.querySelectorAll('.reveal.active').length")
        print(f"Active reveals after scroll: {active_reveals}")

        browser.close()

if __name__ == "__main__":
    test_scroll_animations()
