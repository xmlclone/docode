1. compat: 兼容，比如 compat.py 里面可以定义一些 python 或 库 版本相关的判断
2. deco(decorator): 装饰器，比如 deco.py   wrapper
3. expected_status
4. max_retries
5. disable_warnings
6. convert_to_boolean
7. register fire add_listener remove_listener
8. Helper method to check HTTP status
9. utils.py
10. model 数据模型 dao 数据模型基础操作 service 业务逻辑处理 controller 处理用户请求
11. constant.py 常量
12. exception.py
13. events.py
14. Environment
15. plugin 插件
16. Rule Severity  等级
17. I18N 是指国际化（Internationalization），而 L10N 是指本地化（Localization），都是每个单词的第一个和最后一个字母，中间的数字是每个单词中间字母的数量
18. Attachement 附件


```py
class ResultStatus(Enum):
    Failure = 'Failure'
    Success = 'ss'
```