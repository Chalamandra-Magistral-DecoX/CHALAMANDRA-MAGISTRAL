import asyncio
from playwright.async_api import async_playwright
import subprocess
import time
import os

async def run():
    server = subprocess.Popen(["python3", "-m", "http.server", "8000"])
    time.sleep(1)

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Ignore 404 for Vercel insights
            page.route("**/_vercel/insights/script.js", lambda route: route.abort())

            print("Navigating to http://localhost:8000/index.html")
            await page.goto("http://localhost:8000/index.html", wait_until="networkidle")

            # Check initial state
            print("Checking initial state...")
            progress_bar = await page.evaluate("document.getElementById('scroll-progress').style.width")
            print(f"Initial progress bar width: {progress_bar}")

            srap_section = page.locator("#srap")
            is_active_initially = await srap_section.evaluate("el => el.classList.contains('active')")
            print(f"Is #srap active initially? {is_active_initially}")

            # Scroll down slowly to trigger intersection observer
            print("Scrolling down...")
            for y in range(0, 3000, 100):
                await page.evaluate(f"window.scrollTo(0, {y})")
                await page.wait_for_timeout(50)

            await page.wait_for_timeout(1000)

            # Check state after scroll
            print("Checking state after scroll...")
            progress_bar_after = await page.evaluate("document.getElementById('scroll-progress').style.width")
            print(f"Progress bar width after scroll: {progress_bar_after}")

            is_active_after = await srap_section.evaluate("el => el.classList.contains('active')")
            print(f"Is #srap active after scroll? {is_active_after}")

            if progress_bar != progress_bar_after and is_active_after:
                print("Verification PASSED: Scroll progress updated and element was revealed.")
            else:
                print("Verification FAILED: Scroll behavior did not work as expected.")

            await browser.close()
    finally:
        server.terminate()

if __name__ == "__main__":
    asyncio.run(run())
