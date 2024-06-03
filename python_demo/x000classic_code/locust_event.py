import logging
import traceback


class EventHook:
    def __init__(self):
        self._handlers = []

    def add_listener(self, handler):
        self._handlers.append(handler)
        return handler

    def remove_listener(self, handler):
        self._handlers.remove(handler)

    # 用 * 占用首个参数，那么此方法只能接收关键字方式的调用
    def fire(self, *, reverse=False, **kwargs):
        if reverse:
            handlers = reversed(self._handlers)
        else:
            handlers = self._handlers
        for handler in handlers:
            try:
                handler(**kwargs)
            except Exception:
                logging.error("Uncaught exception in event handler: \n%s", traceback.format_exc())


class DeprecatedEventHook(EventHook):
    def __init__(self, message):
        self.message = message
        logging.warning(self.message)
        super().__init__()

    def add_listener(self, handler):
        logging.warning(self.message)
        return super().add_listener(handler)


class Events:

    """event1 和 event2 分别演示不同参数数量的情况"""

    """
    :param arg1
    :param arg2
    """
    event1: EventHook

    """
    :param arg1
    :param arg2
    :param arg3
    """
    event2: EventHook


    """演示下面 vars 的逻辑，注意不能定义为 EventHook() """
    event3 = EventHook

    event4: DeprecatedEventHook


    def __init__(self):
        # vars 返回的就是对象的 __dict__ 属性， key 是变量名， value 是类型
        # 这里这样做的目的是为了应对上面 event3 的定义方式
        # https://docs.python.org/3/library/functions.html#vars
        for name, value in vars(type(self)).items():
            if value == EventHook:
                print(f"vars: {name=}, {value=}")
                # 注意这里的是 value() ，即把对应的 EventHook 初始化了
                setattr(self, name, value())
            # 处理已经被废弃的事件
            elif value == DeprecatedEventHook:
                setattr(self, name, value(f"{name} Event is DEPRECATED."))

        # self.__annotations__ 返回的就是具有类型标注的字典对象，key 是变量名， value 是标注的类型
        for name, value in self.__annotations__.items():
            if value == EventHook:
                print(f"annotations: {name=}, {value=}")
                setattr(self, name, value())
            # 处理已经被废弃的事件
            elif value == DeprecatedEventHook:
                setattr(self, name, value(f"{name} Event is DEPRECATED."))


# 全局初始化一个 event 对象，一般建议在包的 __init__ 里面全局初始化
events = Events()

# 对某个事件增加监听器
events.event1.add_listener(lambda x, y: print(f"{x=}, {y=}"))

# 在合适的地方触发这个事件
events.event1.fire(x=1, y=2)
