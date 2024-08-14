import requests


# 请求 https://www.codegeex.cn/ 网站，获取返回响应状态、响应头、响应内容，并输出

def get_response(url):
    response = requests.get(url)
    return response
response = get_response('https://www.codegeex.cn/')
print('状态码：', response.status_code)
print('响应头：', response.headers)
print('响应内容：', response.text)
# 输出响应状态码
print('状态码：', response.status_code)

# 输出响应头
print('响应头：', response.headers)


# 调用selenium打开google浏览器访问百度首页

from selenium import webdriver
# 创建一个Chrome浏览器实例
driver = webdriver.Chrome()

# 打开百度首页
driver.get('https://www.baidu.com')
# 输出当前页面的标题
print(driver.title)

# 关闭浏览器
driver.quit()


# 使用pytest编写一个测试函数的示例

import pytest
def add(x, y):
    return x + y


def test_add():
    assert add(1, 2) == 3
    assert add(3, 5) == 8
    assert add(2, 4) == 6


# 使用pytest编写一个测试类示例

import pytest


class TestAdd:
    def test_add(self):
        assert add(1, 2) == 3
        assert add(3, 5) == 8
        assert add(2, 4) == 6

    def test_add_negative(self):
        with pytest.raises(AssertionError):
            add(1, 2)
            