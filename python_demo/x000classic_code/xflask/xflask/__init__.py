import os
import logging

from flask import Flask
from pathlib import Path

from .log import config_logger


config_logger()
logger = logging.getLogger(__name__)


def register_plugin(app: Flask):
    from .model import init_app as model_init_app
    from .command import init_app as command_init_app
    from .error import init_app as error_init_app
    from .service import init_app as service_init_app

    for plugin in [
        model_init_app,
        command_init_app,
        error_init_app,
        service_init_app,
    ]:
        plugin(app)


def create_app(config_name='default'):
    logger.debug(f"{config_name=}")
    app = Flask(
        __name__, 
        instance_relative_config=True, 
        instance_path=str(Path('.').absolute() / 'instance')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    if config_name == 'prod':
        app.config.from_pyfile('config_prod.py')
    elif config_name == 'test':
        app.config.from_pyfile('config_test.py')
    elif config_name == 'dev':
        app.config.from_pyfile('config_dev.py')
    else:
        app.config.from_pyfile('config.py')

    # register plugin
    register_plugin(app)

    return app