*** Settings ***
Documentation    模块内部测试数据


*** Variables ***
# 支持搜索的中文、邮箱前缀、花名等
${CN_NAME}    林磊
${MAIL_PREFIX}    linlei
${ALIAS_NAME}    龙舟
${CN_ALIAS_NAME}    ${CN_NAME}(${ALIAS_NAME})
