import re

"""
S 任何非空字符
s 任何空白字符
w 任何字母、数字、下划线
W 任意不是字母、数字或下划线
d 数字
. 任意字符，如果没有指定 re.S 是无法匹配换行的，如果匹配换行，需要指定 re.S
* 任意多次
? 0或1次
+ 1或多次

re.I 忽略大小写
re.S 指定 . 可以匹配换行
re.M 如果指定， ^$ 会对每行进行开头和结尾匹配，未指定此标志， ^$ 只会匹配整个字符串的开头和结尾
re.I | re.M | re.S 多个条件
"""


message = """
POST Response : url=https://jadeite.migu.cn/read_search/storeSearch
status=200, reason=OK
headers={'Server': 'nginx', 'Date': 'Wed, 05 Jun 2024 03:16:59 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Content-Length': '15', 'Connection': 'keep-alive', 'Vary': 'Access-Control-Request-Headers'}
body={
    "code":800
}
"""


# groupdict re.S . 匹配换行
match = re.search(r"url=(?P<url>\S+).*status=(?P<status>\d+).*body=(?P<body>.*)", message, re.S)
if match:
    print(match.groupdict())

print('-' * 200)

# search 是从匹配的地方开始查找，即不是完全匹配
match = re.search(r"url=(\S+)", message)
if match:
    # match=<re.Match object; span=(17, 68), 
    # match='url=https://jadeite.migu.cn/read_search/storeSear>, 
    # match.group(0)='url=https://jadeite.migu.cn/read_search/storeSearch', 
    # match.group(1)='https://jadeite.migu.cn/read_search/storeSearch', 
    # ('https://jadeite.migu.cn/read_search/storeSearch',)
    # group(0) 获取到的是所有匹配的字符串，从 group(1) 开始才是分组(即()包裹)的内容
    print(f"{match=}, {match.group(0)=}, {match.group(1)=}, {match.groups()}")

# match 必须从最开始就需要进行匹配
match = re.match(r"url=(\S+)", "POST Response : url=https://jadeite.migu.cn/read_search/storeSearch")
print(match) # None ，这里无法匹配

match = re.match(r".*url=(\S+)", "POST Response : url=https://jadeite.migu.cn/read_search/storeSearch")
print(match) # 这里可以匹配


message = "Hello, my name is python, version is 3.7.0, you can use bigger than 3.7.0, thank you!"
re_compile = re.compile(r"(\d\.\d\.\d)")
# search 只会匹配到最开头的值
match = re.search(re_compile, message)
if match:
    print(match.groups())

# findall 会返回所有匹配的值，返回是列表
match = re.findall(re_compile, message)
print(match)

# version 进行命名
match = re.search(r"version is (?P<version>\d\.\d\.\d), .*(?P=version)", message)
if match:
    # 其中 group(1) 和 group('version') 是一致的
    print(f"{match.group(0)=}, {match.group(1)=}, {match.group('version')=}, {match.groupdict()=}")


# 贪婪与非贪婪
message = '"This message contains"you can get it."'
# 这是贪婪模式，即匹配到最后一个"
ret = re.search(f'"This message .*"', message)
print(ret)
# 这是非贪婪模式，匹配到contains后的"即停止
ret = re.search(f'"This message .*?"', message)
print(ret)

# 原始字符串  re.compile
message = 'This message contains [, you can get it.'
# 注意这里不管是否有 r, 匹配[, 需要使用\[，建议下面的写法，不要省略r和\
ret = re.search(r'\[, (.*)', message)
print(ret)
re_compile = re.compile(r'\[, (.*)', re.I)
ret = re_compile.search(message)
print(ret)