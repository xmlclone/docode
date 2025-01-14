from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(
        executable_path='/root/.cache/ms-playwright/chromium-1134/chrome-linux/chrome'
    )
    page = browser.new_page()
    # page.goto("https://www.baidu.com")
    page.goto("https://www.migu.cn/main/")
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



# 另外一种方式
pw = sync_playwright().start()
chromium = pw.chromium
browser = chromium.launch(executable_path='/root/.cache/ms-playwright/chromium-1134/chrome-linux/chrome')
page = browser.new_page()
page.goto("https://www.migu.cn/main/")
browser.close()
pw.stop()