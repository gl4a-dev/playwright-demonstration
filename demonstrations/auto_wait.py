import re
from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        print("Navigating to a page with slow loading...")
        page.goto("https://demo.playwright.dev/todomvc/#/")

        print("Trying to interact with an element that hasn't exist yet...")
        input_box = page.locator('input.new-todo')
        
        input_box.fill("Learn Playwright")
        input_box.press("Enter")

        print("Interaction concluded successfully.")
        
        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    run()