from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Intercept and abort the script request causing errors
        def handle_route(route):
            if '/_vercel/insights/script.js' in route.request.url:
                route.abort()
            else:
                route.continue_()

        page.route("**/*", handle_route)

        # Navigate to the page
        page.goto('http://localhost:8000/')

        # Wait for the page to be loaded completely
        page.wait_for_load_state('networkidle')

        # Get target element location
        reveal_elem = page.locator('#srap')
        box = reveal_elem.bounding_box()
        # Scroll down incrementally to ensure we trigger the intersection observer correctly
        page.evaluate(f'window.scrollTo(0, {box["y"] - 100})')
        page.wait_for_timeout(500)
        page.evaluate(f'window.scrollTo(0, {box["y"]})')
        page.wait_for_timeout(500)
        page.evaluate(f'window.scrollTo(0, {box["y"] + 200})')
        page.wait_for_timeout(500)

        # Take a screenshot
        page.screenshot(path='verification/scroll_verification.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    main()
