import logging
import traceback

from functools import wraps


logger = logging.getLogger(__name__)


def catch_exc_return_false(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            logger.warning(e)
            logger.debug(traceback.format_exc())
            return False
        else:
            return True
    return wrap