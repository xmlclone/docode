import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By



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
# 另外可以写一个简单的自己的等待方法
def wait_until_element(by, value, timeout=5, interval=0.1):
    epochs = int(timeout / interval)
    for _ in range(epochs):
        try:
            element = driver.find_element(by, value)
        except:
            time.sleep(interval)
        else:
            return element
    else:
        return None

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
# 根据class name匹配，如果元素有多个css，指定一个即可，无法指定多个，元素类似: <p class="header-search-button">
# 注意这里不需要使用.或#，直接使用class的name即可
element = driver.find_element(By.CLASS_NAME, 'header-search-button')

# 关闭当前页面
driver.close()
# 退出整个程序
driver.quit()