from playwright.sync_api import sync_playwright, Playwright


# 另外一种方式
pw = sync_playwright().start()
chromium = pw.chromium
browser = chromium.launch()
page = browser.new_page()
page.goto("https://www.baidu.com")

page.screenshot(path='1.png')

browser.close()
pw.stop()