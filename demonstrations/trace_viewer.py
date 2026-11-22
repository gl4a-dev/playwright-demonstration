from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = browser.new_context(
            record_video_dir="demonstrations/videos/",
            record_har_path="demonstrations/network.har"
        )

        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()

        try:
            print("Accessing page...")
            page.goto("https://playwright.dev/")

            print("Clicking in 'Docs'...")
            page.get_by_role("link", name="Docs").click()

            # --- FALHA PROPOSITAL ---
            print("Trying to find an inexistent element (will fail)...")
            page.locator("text=GhostElement123456").click(timeout=2000)

        except Exception as e:
            print(f"Test failed: {e}")

        finally:
            trace_path = "demonstrations/trace.zip"
            context.tracing.stop(path=trace_path)
            print(f"File saved on: {trace_path}")

            context.close()
            browser.close()

if __name__ == "__main__":
    run()