*** Settings ***
Documentation    配置文件


*** Variables ***
# 慢速运行，方便查看与定位，可以直接指定数字，单位为秒，一般设置为0.5s即可
# 当不需要时请指定为${Empty}；在正式执行时，应该设置为${Empty}
${SLOW}    0.5s
# SeleniumLibrary库Wait...相关关键字的超时时间，建议配置为5s
${TIMEOUT}    5s
# 隐式等待元素定位或操作的超时时间，建议配置为3s
${IMPLICIT_TIMEOUT}    3s

