*** Settings ***
Documentation    元素定位器


*** Variables ***
# ==================== 通用元素 ====================
${E_COMMON_LOGOUT}    link:退出    # 退出账户

# ==================== 登录页元素 ====================
${E_LOGIN_IFRAME}    id:logonIframe    # 登录页嵌套的iframe
${E_LOGIN_USERNAME}    id:wenb    # 用户名输入框
${E_LOGIN_PASSWORD}    id:worde    # 密码输入框
${E_LOGIN_LOGIN}    id:submitButton    # 登录按钮
${E_LOGIN_FORGETPASSWORD}    class:forgetPassword    # 忘记密码

# ==================== OA首页元素 ====================
${E_INDEX_ADDRESSBOOK}    link:公司通讯录    # 通讯录

# ==================== 通讯录页面元素 ====================
${E_ADDRESSBOOK_SEARCH_INPUT}    id:searchcond    # 搜索框
${E_ADDRESSBOOK_SEARCH_BUTTON}    id:search    # 搜索按钮
