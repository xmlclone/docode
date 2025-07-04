import click
from .models import db


@click.command('init-db', help='初始化数据库')
def init_db():
    db.drop_all()
    db.create_all()
