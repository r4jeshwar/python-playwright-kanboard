from playwright.sync_api import Playwright, sync_playwright, expect

def change_password(playwright: Playwright) -> None:
    PASSWORD = os.environ.get("PASSWORD")
    CONFIRM_PASS = os.environ.get("CONFIRM_PASS")
    URL = os.environ.get("URL")
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":800,"height":600})
    page = context.new_page()
    page.goto(URL)
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("admin")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("admin")
    page.locator("text=Sign in").click()
    page.locator("[aria-label=\"admin\"]").click()
    page.locator("#dropdown li:has-text(\"My profile\")").click()
    page.locator("text-Change password").click()
    page.locator("input[name=\"current_password\"]").click()
    page.locator("input[name=\"current_password\"]").fill("PASSWORD")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("CONFIRM_PASS")
    page.locator("fieldset").click()
    page.locator("input[name=\"confirmation\"]").click()
    page.locator("input[name=\"confirmation\"]").fill("CONFIRM_PASS")
    page.locator("text=Save").click()
    page.wait_for_timeout=(5000)
    context.close()
    browser.close()
    
with sync_playwright() as playwright:
    change_password(playwright)