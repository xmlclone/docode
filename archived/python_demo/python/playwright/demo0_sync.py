from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


# 另外一种方式
pw = sync_playwright().start()
chromium = pw.chromium
browser = chromium.launch()
page = browser.new_page()
page.goto("https://www.baidu.com")
browser.close()
pw.stop()