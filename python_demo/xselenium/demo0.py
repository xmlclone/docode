import time
from selenium.webdriver import Chrome, ChromeOptions

url = 'https://www.baidu.com/'
# 列举常用的一些chrome选项
# 注意：各浏览器支持的配置项可能不一致，比如firefox的代理配置和chrome是不同的
chrome_option = ChromeOptions()
for option in [
    '--headless', # 无头模式启动
    '--no-sandbox',
]:
    chrome_option.add_argument(option)
driver = Chrome(options=chrome_option)
# 打开浏览器并访问指定的url
driver.get(url)
time.sleep(3)
# 必须是png后缀
driver.get_screenshot_as_file('test1.png')
# 关闭当前页面
driver.close()
# 退出整个程序
driver.quit()