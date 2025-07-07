import logging
import warnings
import traceback


class EventHook:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self._handlers = []

    def add_listener(self, handler):
        self._handlers.append(handler)
        return handler

    def remove_listener(self, handler):
        self._handlers.remove(handler)

    def fire(self, *, reverse=False, **kwargs):
        # 只接收关键字方式传递
        if reverse:
            handlers = reversed(self._handlers)
        else:
            handlers = self._handlers
        for handler in handlers:
            try:
                handler(**kwargs)
            except Exception:
                self.logger.error("Uncaught exception in event handler: \n%s", traceback.format_exc())


class DeprecatedEventHook(EventHook):
    def __init__(self, message):
        self.message = message
        logging.warning(self.message)
        super().__init__()

    def add_listener(self, handler):
        logging.warning(self.message)
        return super().add_listener(handler)


class Events:
    """事件类"""

    """框架异常
    :param e Exception
    """
    fw_exception: EventHook

    def __init__(self):
        for name, value in vars(type(self)).items():
            if value == EventHook:
                setattr(self, name, value())
            elif value == DeprecatedEventHook:
                setattr(self, name, value(f"{name} Event is DEPRECATED."))

        for name, value in self.__annotations__.items():
            if value == EventHook:
                setattr(self, name, value())
            elif value == DeprecatedEventHook:
                setattr(self, name, value(f"{name} Event is DEPRECATED."))


events = Events()


def fw_exception_handler(e: Exception):
    warnings.warn(e)


events.fw_exception.add_listener(fw_exception_handler)


if __name__ == '__main__':
    try:
        1 / 0
    except Exception as e:
        # 必须通过关键字参数方式传递
        events.fw_exception.fire(e=e)
