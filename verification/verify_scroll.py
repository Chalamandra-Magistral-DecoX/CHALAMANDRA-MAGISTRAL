from playwright.sync_api import sync_playwright

def verify_scroll(page):
    # Abort vercel insights to avoid 404 errors as per memory guidelines
    page.route("**/_vercel/insights/script.js", lambda route: route.abort())

    page.goto('http://localhost:8080/index.html')
    page.wait_for_load_state('networkidle')

    # Scroll down to trigger reveals and progress bar update
    page.evaluate("window.scrollBy(0, window.innerHeight)")
    page.wait_for_timeout(500) # Wait for animation frame and observer

    page.screenshot(path="verification/scroll_verification.png", full_page=True)

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify_scroll(page)
        finally:
            browser.close()
