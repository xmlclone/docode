import os
import logging
from flask import Flask
from .config import Config
from .log import setup_logger
from .cli import init_db
from .urls import configure_urls
from .auth import configure_auth
from .models import configure_models


logger = logging.getLogger(__name__)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    for configure_func in [
        configure_app,
        configure_logging,
        configure_urls,
        configure_cli,
        configure_auth,
        configure_models
    ]:
        configure_func(app)
    return app


def configure_app(app: Flask):
    try: os.makedirs(app.instance_path)
    except OSError: pass


def configure_logging(app: Flask):
    setup_logger(app)


def configure_cli(app: Flask):
    app.cli.add_command(init_db)