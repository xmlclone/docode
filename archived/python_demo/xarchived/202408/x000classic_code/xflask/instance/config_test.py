from pathlib import Path


SECRET_KEY = 'test'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path('.').absolute()/ 'instance' / 'xflask.db'}"
DEBUG = True