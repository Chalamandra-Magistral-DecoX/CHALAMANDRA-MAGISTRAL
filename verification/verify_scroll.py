from playwright.sync_api import sync_playwright

def verify_frontend(page):
    page.goto("http://localhost:8000")

    # Wait for the main page to load
    page.wait_for_selector('h1')

    # Scroll down to trigger the reveal animations
    page.evaluate("window.scrollTo(0, 1000)")
    page.wait_for_timeout(1000)
    page.evaluate("window.scrollTo(0, 2000)")
    page.wait_for_timeout(1000)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Wait for a bit to let animations and requestAnimationFrame settle
    page.wait_for_timeout(2000)

    # Check if a reveal element has the 'active' class
    reveal_elements = page.locator('.reveal').all()
    for i, el in enumerate(reveal_elements):
        is_active = el.evaluate("e => e.classList.contains('active')")
        print(f"Reveal element {i} active: {is_active}")

    # Take a screenshot
    page.screenshot(path="verification/scroll_optimized.png", full_page=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            # Ignore 404s from Vercel analytics
            page.route("**/_vercel/insights/script.js", lambda route: route.abort())
            verify_frontend(page)
        finally:
            browser.close()