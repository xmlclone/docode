import click
import logging

from flask import Flask

from .model import db


logger = logging.getLogger(__name__)


def init_app(app: Flask):
    app.cli.add_command(test_init_db)


@click.command('test-init-db', help="初始化DB(请勿在生成环境使用)")
def test_init_db():
    logger.debug(f"test-init-db: {db=}")
    db.drop_all()
    db.create_all()