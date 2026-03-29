import asyncio
from playwright.async_api import async_playwright
import time

async def test_scroll():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Abort vercel insights to avoid 404 errors as per memory guidelines
        await page.route("**/_vercel/insights/script.js", lambda route: route.abort())

        await page.goto('http://localhost:8080/index.html')
        await page.wait_for_load_state('networkidle')

        # Initial check
        print("Page loaded.")

        # Scroll down to trigger reveals and progress bar update
        await page.evaluate("window.scrollBy(0, window.innerHeight)")
        await page.wait_for_timeout(500)

        # Check progress bar width
        progress_width = await page.evaluate("document.getElementById('scroll-progress').style.width")
        print(f"Scroll progress width after scroll: {progress_width}")

        # Scroll more to trigger reveals
        await page.evaluate("window.scrollBy(0, window.innerHeight * 2)")
        await page.wait_for_timeout(1000)

        # Check if reveals are active
        active_reveals = await page.evaluate("document.querySelectorAll('.reveal.active').length")
        total_reveals = await page.evaluate("document.querySelectorAll('.reveal').length")
        print(f"Active reveals: {active_reveals} / {total_reveals}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(test_scroll())
