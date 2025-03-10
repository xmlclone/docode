import logging
import pandas as pd

from ccode.logger import config_logging


config_logging(
    console_level=logging.DEBUG,
    convert_newline=False,
)
logger = logging.getLogger(__name__)


def read_excel(filepath):
    df = pd.read_excel(filepath)
    return df


if __name__ == '__main__':
    df = read_excel('pandas_data.xlsx')
    logger.debug(f"\n{df}")
