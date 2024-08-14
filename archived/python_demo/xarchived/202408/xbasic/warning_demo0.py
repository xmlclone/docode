import warnings

# https://docs.python.org/3/library/warnings.html


"default"
"error"
"ignore"
"always"
"module"
"once"


# 忽略所有 warning
# 等同于 python -W ignore demo0.py
# warnings.filterwarnings("ignore")

# 忽略指定的 warning
# 等同于 python -W ignore::UserWarning demo0.py
# warnings.filterwarnings("ignore", category=UserWarning)

# 把指定告警转换为 error, 一旦遇到 UserWarning 的告警，则直接抛出异常
# 等同于 python -W error::UserWarning demo0.py
# warnings.filterwarnings("error", category=UserWarning)


# 第一个参数是 message ， 第二个参数是 category
warnings.warn("UserWarning Message", UserWarning)
warnings.warn("DeprecationWarning Message", DeprecationWarning)
warnings.warn("SyntaxWarning Message", SyntaxWarning)
warnings.warn("RuntimeWarning Message", RuntimeWarning)
warnings.warn("FutureWarning Message", FutureWarning)
warnings.warn("PendingDeprecationWarning Message", PendingDeprecationWarning)
warnings.warn("ImportWarning Message", ImportWarning)
warnings.warn("UnicodeWarning Message", UnicodeWarning)
warnings.warn("BytesWarning Message", BytesWarning)
warnings.warn("ResourceWarning Message", ResourceWarning)