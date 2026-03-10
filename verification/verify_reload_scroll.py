from playwright.sync_api import sync_playwright
import time

def verify_reload_scroll():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Create a new context to persist state (like scroll position across reloads)
        context = browser.new_context()
        page = context.new_page()

        print("Navigating to index.html...")
        page.goto("http://localhost:8000/index.html")
        page.wait_for_load_state("networkidle")

        # Scroll down
        print("Scrolling down...")
        page.evaluate("window.scrollTo(0, 1500)")
        time.sleep(1)

        # Reload the page
        print("Reloading page...")
        page.reload()
        page.wait_for_load_state("networkidle")
        time.sleep(1)

        # Check if '.reveal' elements above fold are active after reload
        reveal_elements_active = page.evaluate('''() => {
            const reveals = document.querySelectorAll('.reveal');
            let activeCount = 0;
            for(let r of reveals) {
                if (r.classList.contains('active')) activeCount++;
            }
            return activeCount;
        }''')

        print(f"Found {reveal_elements_active} '.reveal' elements with '.active' class after reload.")
        if reveal_elements_active == 0:
            print("❌ Reveal elements above the fold did not become active after reload!")
        else:
            print("✅ Edge case handled correctly: elements active on reload.")

        browser.close()

if __name__ == "__main__":
    verify_reload_scroll()
