*** Settings ***
# 本地没有安装requests库
Library    Remote    http://127.0.0.1:8270    AS    lib1


*** Test Cases ***
Case1
    # 发起get请求
    ${ret}    Get    http://t.weather.sojson.com/api/weather/city/101030100
    Log    ${ret}