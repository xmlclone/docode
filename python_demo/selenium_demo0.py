'''
环境：
conda create -n vdocode python=3.12
selenium==4.14.0

链接：
api接口文档: https://www.selenium.dev/selenium/docs/api/py/py-modindex.html
最佳实践(包括PO页面对象模型等): https://www.selenium.dev/zh-cn/documentation/test_practices/design_strategies/
chrome选项参数大全: https://peter.sh/experiments/chromium-command-line-switches/
xpath教程: https://www.w3school.com.cn/xpath/index.asp

基本原理:
driver启动后(比如chromedriver)，会与浏览器建立websocket的链接，并且提供http服务
客户端(selenium)的各种动作，通过http请求发送到driver，由driver发送给浏览器并返回
'''


import time
import logging.config

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(lineno)d]:  %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
})


url = 'https://github.com/'


# 列举常用的一些chrome选项
# 注意：各浏览器支持的配置项可能不一致，比如firefox的代理配置和chrome是不同的
chrome_option = ChromeOptions()
for option in [
    '--headless', # 无头模式启动

    # 如果需要访问设备的摄像头、麦克风，但我们如果不想使用真实的，可以通过以下方式进行模拟
    # '--use-fake-ui-for-media-stream',
    # '--use-fake-device-for-media-stream',
    # '--allow-file-access-from-files',
    # '--use-file-for-fake-video-capture=path/to/video.y4m',  # 模拟的摄像头画面的视频文件
    # '--use-file-for-fake-audio-capture=path/to/audio.wav', # 模拟的麦克风的音频文件

    # '--proxy-server=127.0.0.1:7890', # 配置代理
]:
    chrome_option.add_argument(option)

driver = Chrome(options=chrome_option)
# 打开浏览器并访问指定的url
driver.get(url)

# 最大化窗口
driver.maximize_window()

# 等待的几种方式
# 方式一，强制等待指定的时间，不推荐，浪费时间
# time.sleep(5)
# 方式二，指定等待的最长时间，一旦查找成功则返回
driver.implicitly_wait(5)
# 方式三，wait.until方式
wait = WebDriverWait(driver, 5)
# until第一个参数是一个函数，函数有1个参数(driver)，在指定时间内，函数返回真则成功，否则抛出异常 TimeoutException
wait.until(lambda _: 'GitHub' in driver.title)
# 方式四，EC方式，需要WebDriverWait配合
# 注意EC模块的大部分函数返回的仍然是一个函数，并且接受一个driver参数，和方式三一样，故这里不需要写成函数或lambda的方式了
wait.until(EC.title_contains('GitHub'))

# 查找元素的几种方式(最简单的就是By.ID，这里不做演示)
# 如果无法查找到指定的元素，这里的超时时间是根据driver.implicitly_wait(5)设定的时间，则抛出 NoSuchElementException
element = driver.find_element(By.XPATH, '//a[contains(text(), "Sign in")]')
elements = driver.find_elements(By.TAG_NAME, 'div')
# find_element只会返回找到的第一个元素
element = driver.find_element(By.TAG_NAME, 'div')
# Xpath根据元素属性查找
element = driver.find_element(By.XPATH, '//button[@placeholder="Search or jump to..."]')
# 根据css selector匹配
element = driver.find_element(By.CSS_SELECTOR, 'button.header-search-button')
# 根据class name匹配，如果元素有多个css，指定一个即可，无法指定多个
element = driver.find_element(By.CLASS_NAME, 'header-search-button')

# 元素访问
# element.click()
# element.send_keys("123456")
# element.get_attribute('placeholder')
# element.text

# driver属性访问
# driver.title
# driver.current_url
# driver.current_window_handle

# 动作

# 截屏
# 必须是png后缀
driver.get_screenshot_as_file('test1.png')
with open('test2.png', 'wb') as fp:
    # 返回的是bytes，故需要写入文件
    fp.write(driver.get_screenshot_as_png())
# 返回的是base64字符串，可以直接写入到html文件用于展示
with open('test3.html', 'w') as fp:
    fp.write(f'<img src="data:image/png;base64, {driver.get_screenshot_as_base64()}" alt="嵌入的图像">')
# 内部就是直接调用了get_screenshot_as_file
driver.save_screenshot('test4.png')

# 多窗口处理(切换窗口)
# driver.current_window_handle
# for handle in driver.window_handles:
#     if driver.current_window_handle != handle:
#         driver.switch_to.window(handle)
#         break

# cookie

# 执行脚本

# 回调监听

# input('Press any key to exit.')
# 关闭当前页面
driver.close()
# 退出整个程序
driver.quit()