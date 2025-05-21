import os
import logging
from flask import Flask, render_template
from .config import Config
from .log import setup_logger
from .cli import init_db
from .auth import configure_plugin_login_manager
from .models import configure_plugin_sqlalchemy


logger = logging.getLogger(__name__)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    for configure_func in [
        configure_app,
        configure_logging,
        configure_routes,
        configure_plugins,
        configure_cli
    ]:
        configure_func(app)
    # logger.debug(f'{app.secret_key=}, {app.instance_path=}')
    # logger.debug(f'{app.jinja_loader.searchpath=}')
    return app


def configure_app(app: Flask):
    try: os.makedirs(app.instance_path)
    except OSError: pass


def configure_logging(app: Flask):
    setup_logger(app)


def configure_routes(app: Flask):
    from .routes.main import main_bp
    from .routes.auth import auth_bp
    for bp in [
        main_bp,
        auth_bp
    ]:
        app.register_blueprint(bp)


def configure_plugins(app: Flask):
    for configure_func in [
        configure_plugin_login_manager,
        configure_plugin_sqlalchemy
    ]:
        configure_func(app)


def configure_cli(app: Flask):
    app.cli.add_command(init_db)