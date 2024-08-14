"""
pip install pytest-playwright


# 安装自带的浏览器
playwright install

# 卸载
playwright uninstall --all

# 安装指定的浏览器
playwright install webkit

# 安装系统依赖
playwright install-deps
playwright install-deps chromium

# 也可以一键安装浏览器和依赖
playwright install --with-deps chromium


1. autowaiting机制: https://playwright.dev/python/docs/actionability
2. 元素可见、稳定、接收事件、可用、可编辑: https://playwright.dev/python/docs/actionability#introduction
3. 元素的状态判断(expect.to_be_xxx): 
    https://playwright.dev/python/docs/actionability#assertions
    https://playwright.dev/python/docs/test-assertions#list-of-assertions
4. expect配置
    自定义消息: https://playwright.dev/python/docs/test-assertions#custom-expect-message
    超时时间: https://playwright.dev/python/docs/test-assertions#setting-a-custom-timeout

安装代理配置: https://playwright.dev/python/docs/browsers#install-behind-a-firewall-or-a-proxy
"""


from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import BrowserType, Browser, Page, ConsoleMessage
from playwright.sync_api import TimeoutError


url = 'http://127.0.0.1:5720/python_demo/xplaywright/demo0.html'
baidu = 'https://www.baidu.com'


with sync_playwright() as playwright:
    # playwright.firefox
    # playwright.webkit
    chrome: BrowserType = playwright.chromium


    browser: Browser = chrome.launch(
        headless=False,
        # 让执行慢下来，调试时使用可以看见程序的操作，单位ms
        slow_mo=1000,
        # 还可以指定浏览器，因为 edge 也使用 chrome 内核，故可以直接使用 chrome 对象
        channel='msedge',
        # 如果不指定此参数，则会用playwright自带的浏览器(前提是通过playwright install安装完成)
        # 如果指定了 executable_path, 那么就以此生效，上面的 channel 不生效
        # executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        executable_path=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    )
    page: Page = browser.new_page()
    page.goto(url)


    # input("open browser console.")


    # ==================================================context==================================================
    # # context让每个context具有独立的 local storage, session storage, cookies etc.
    # context = browser.new_context()
    # page = context.new_page()
    # # 最好的示例
    # user_context = browser.new_context()
    # admin_context = browser.new_context()
    # user_page = user_context.new_page()
    # admin_page = admin_context.new_page()
    # user_page.goto(url)
    # admin_page.goto(baidu)


    # ==================================================录屏==================================================
    # context = browser.new_context(record_video_dir='videos/')
    # with browser.new_context(record_video_dir='videos/') as context:
    #     _page = context.new_page()
    #     _page.goto(url)
    #     _page.wait_for_timeout(2000)
    #     _page.locator('id=demo0').fill('abcdef')
    #     _page.wait_for_timeout(2000)


    # ==================================================trace==================================================
    # with browser.new_context(record_video_dir='videos/') as context:
    #     context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #     _page = context.new_page()
    #     _page.goto(url)
    #     _page.wait_for_timeout(2000)
    #     _page.locator('id=demo0').fill('abcdef')
    #     _page.wait_for_timeout(2000)
    #     context.tracing.stop(path = "trace.zip")
        # 最后使用 playwright show-trace trace.zip 命令打开


    # ==================================================全局超时==================================================
    # # 默认 30000ms
    page.set_default_timeout(3000)
    # # expect 默认超时时间 5000 ms
    # expect.set_options(timeout=3000)


    # ==================================================硬等待==================================================
    # # 使用page.wait_for_timeout代替time.sleep，尽量不要使用time.sleep，因为playwright内部用到了async机制
    # page.wait_for_timeout(1000)


    # ==================================================截图==================================================
    # page.screenshot(path='1.png')


    # ==================================================事件==================================================
    # with page.expect_popup() as popup:
    #     page.get_by_text("open the popup").click()
    # popup.value.goto(url)

    def print_console_message(console_message: ConsoleMessage):
        print(console_message.text)
    page.on("console", print_console_message)

    # ===================增加和移除自定义监听===================
    # def print_request_sent(request):
    #     print("Request sent: " + request.url)

    # def print_request_finished(request):
    #     print("Request finished: " + request.url)

    # page.on("request", print_request_sent)
    # page.on("requestfinished", print_request_finished)
    # page.goto(baidu)

    # page.remove_listener("requestfinished", print_request_finished)
    # page.goto(baidu)


    # ==================================================expect==================================================


    # ==================================================元素定位与操作==================================================
    # 用于具有 aria-label 或 label for 元素定位
    # 所有元素定义，即 get_by_label 或 locator 默认情况下不会执行真正的查找，而是在有动作时(比如fill clear等情况下)才触发查找
    # 故 get_by_label 等这些方法并不会报错

    # ===================常用定位方法及过滤===================
    # # https://playwright.dev/python/docs/locators
    # # <button>Sign in</button>
    # # 注意这里的 name 参数不是根据元素的 name 属性查找，而是元素的 text 查找
    # page.get_by_role("button", name="Sign in").click()

    # # <span>Welcome, John</span>
    # page.get_by_text("Welcome, John")  # 默认是包含，可以通过 exact=True 表示完全匹配，还可以使用正则表达式 re.compile

    # page.get_by_label()
    # page.get_by_placeholder()

    # # <img alt="playwright logo" src="/img/playwright-logo.svg" width="100" />
    # page.get_by_alt_text("playwright logo")

    # # <span title='Issues count'>25 issues</span>
    # page.get_by_title("Issues count")

    # # <button data-testid="directions">Itinéraire</button>
    # page.get_by_test_id("directions")

    # # get_by_test_id 默认根据 data-testid 定位，但是可以修改
    # # <button data-pw="directions">Itinéraire</button>
    # playwright.selectors.set_test_id_attribute("data-pw")
    # page.get_by_test_id("directions").click()

    # # css or xpath (not recommended)
    # page.locator("css=button").click()
    # page.locator("xpath=//button").click()
    # page.locator("button").click()
    # page.locator("//button").click()

    # # by id , 下面两种方式都可以
    # page.locator("id=demo3").click()    
    # page.locator("#demo3").click()
    # # by class属性
    # page.locator(".button").click()
    # # 根据元素的属性，比如 name 查找
    # page.locator("button[name='demoName']").click()

    # 过滤: https://playwright.dev/python/docs/locators#filtering-locators
    """
    <ul>
        <li>
            <h3>Product 1</h3>
            <button>Add to cart</button>
        </li>
        <li>
            <h3>Product 2</h3>
            <button>Add to cart</button>
        </li>
    </ul>
    """
    # page.get_by_role("listitem").filter(has_text="Product 2").get_by_role("button", name="Add to cart").click()
    # page.get_by_role("listitem").filter(has_not_text="Out of stock")
    # page.get_by_role("listitem").filter(has=page.get_by_role("heading", name="Product 2")).get_by_role("button", name="Add to cart").click()

    # ===================input===================
    # page.get_by_label('demo0').fill('demo0')
    # page.get_by_label('demo1').fill('demo1')
    # # press_sequentially 会模拟人按序按下(keydown)谈起(keyup)释放(keypress)键盘的各种动作，每个按键都会触发
    # page.get_by_label('demo1').clear()
    # page.get_by_label('demo1').press_sequentially('abcdefg', delay=100)
    
    # ===================radio===================
    # page.get_by_label('demo2').check()
    # expect(page.get_by_label('demo2')).to_be_checked()
    # expect(page.get_by_label('demo2')).not_to_be_checked() # AssertionError:

    # ===================select===================
    # # value or label
    # page.get_by_label('Choose a color').select_option('blue')
    # # only label
    # page.get_by_label('Choose a color').select_option(label='Blue')
    # # Multiple selected
    # page.get_by_label('Choose multiple colors').select_option(['red', 'green', 'blue'])

    # ===================click===================
    # page.get_by_role("button").click()
    # page.get_by_role("button").click(force=True)
    # page.get_by_text("Item").dblclick()
    # page.get_by_text("Item").click(button="right")
    # # shift + click
    # page.get_by_text("Item").click(modifiers=["Shift"])
    # page.get_by_text("Item").hover()
    # # 根据位置点击
    # page.get_by_text("Item").click(position={ "x": 0, "y": 0})

    # ===================press key===================
    # https://playwright.dev/python/docs/input#keys-and-shortcuts
    # page.get_by_text("Submit").press("Enter")
    # # Control+Right
    # page.get_by_role("textbox").press("Control+ArrowRight")
    # page.get_by_role("textbox").press("$")

    # ===================file upload===================
    # # https://playwright.dev/python/docs/input#upload-files
    # page.get_by_label("fileToUpload").set_input_files('1.png')
    # page.locator('.fileToUpload')

    # ===================other===================
    # page.get_by_label('password').focus()
    # page.locator("#item-to-be-dragged").drag_to(page.locator("#item-to-drop-at"))

    # page.locator("#item-to-be-dragged").hover()
    # page.mouse.down()
    # page.locator("#item-to-drop-at").hover()
    # page.mouse.up()

    # page.get_by_text("Footer text").scroll_into_view_if_needed()

    # page.get_by_test_id("scrolling-container").hover()
    # page.mouse.wheel(0, 10)
    # page.get_by_test_id("scrolling-container").evaluate("e => e.scrollTop += 100")


    input('press any key to exit.')