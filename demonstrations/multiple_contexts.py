from playwright.sync_api import sync_playwright, expect
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        # --- User 1 (Admin) ---
        context1 = browser.new_context()
        page1 = context1.new_page()
        page1.goto("https://the-internet.herokuapp.com/login")
        page1.fill("#username", "tomsmith")
        page1.fill("#password", "SuperSecretPassword!")
        page1.click("button[type=submit]")

        expect(page1.locator("h2")).to_contain_text("Secure Area")
        print("Context 1: Logged as TomSmith")
        time.sleep(1) # Pausa para o vídeo

        # --- User 2 (Anonimus) ---
        context2 = browser.new_context()
        page2 = context2.new_page()
        page2.goto("https://the-internet.herokuapp.com/login")
        
        print("Contexto 2: Must be unlogged, even with the Context 1 logged.")
        expect(page2.locator("#username")).to_be_empty()
        
        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    run()