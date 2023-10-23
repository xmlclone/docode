'''
环境：
conda create -n vdocode python=3.12
playwright==1.39.0
playwright install

链接：
文档: https://playwright.dev/python/docs/intro
api: https://playwright.dev/python/docs/api/class-playwright
元素定位: https://playwright.dev/python/docs/locators#locating-elements
元素定位技巧: https://zhuanlan.zhihu.com/p/512646721?utm_id=0
'''

import time

from playwright.sync_api import sync_playwright

'''
本文使用当前目录下的playwright_demo0.html文件作为示例演示
可以结合vscode的live server插件运行一个本地服务
'''

url = 'http://127.0.0.1:5720/python_demo/playwright_demo0.html'

# 启动方式一
with sync_playwright() as playwright:
    chrome = playwright.chromium
    browser = chrome.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    # 单位是ms
    page.set_default_timeout(5000)

    # 元素定位
    element = page.get_by_placeholder("This is placeholder")
    element.fill("test")
    # 查找一个不存在的元素,get_by_xxx的时候并没有真正的去执行，而是在类似click做动作的时候才触发
    # 即正常情况下，get_by_xxx不会抛出异常，而是执行动作时抛出异常
    # page.get_by_text('test').click()
    # playwright提供了get_by_xxx几个查找方法，在selenium里面常用的css xpath需要使用以下方式
    page.locator('xpath=//button[text()="click me"]').click()
    input()
    # by id，注意和下面的css_selector区分
    page.locator('id=id2').click()
    input()
    # by class, 有多个元素可以匹配，需要使用以下方式选择你需要的
    # 类似selenium的By.CSS_SELECTOR而不是CLASS_NAME
    page.locator('.s1').all()[1].click()
    # 等同于下面，playwright自动监测到是css定位，上面xpath类似，可以不用写xpath=
    # page.locator('css=.s1').all()[1].click()
    input()
    # 另外一种css_selector的用法
    page.locator('#id2').click()
    input()


    


    input('Press any key to exit.')

# 启动方式二
# playwright = sync_playwright().start()
# chrome = playwright.chromium
# browser = chrome.launch(headless=False)
# page = browser.new_page()
# page.goto(url)
# input('Press any key to exit.')
# playwright.stop()