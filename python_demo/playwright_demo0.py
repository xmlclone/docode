'''
环境：
conda create -n vdocode python=3.12
playwright==1.39.0
playwright install

链接：
文档: https://playwright.dev/python/docs/intro
api: https://playwright.dev/python/docs/api/class-playwright
元素定位: https://playwright.dev/python/docs/locators#locating-elements
'''

import time

from playwright.sync_api import sync_playwright

url = 'https://github.com/'

# 启动方式一
with sync_playwright() as playwright:
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    # 单位是ms
    page.set_default_timeout(5000)
    element = page.get_by_placeholder("Search or jump to...")
    element.click()
    # 查找一个不存在的元素,get_by_xxx的时候并没有真正的去执行，而是在类似click做动作的时候才触发
    # 即正常情况下，get_by_xxx不会抛出异常，而是执行动作时抛出异常
    # page.get_by_text('test').click()

    # playwright提供了get_by_xxx几个查找方法，在selenium里面常用的css xpath需要使用以下方式
    page.locator('xpath=//button[@placeholder="Search or jump to..."]').click()

    input('Press any key to exit.')

# 启动方式二
# playwright = sync_playwright().start()
# chrome = playwright.chromium
# browser = chrome.launch(headless=False)
# page = browser.new_page()
# page.goto(url)
# input('Press any key to exit.')
# playwright.stop()