from pathlib import Path


SECRET_KEY = 'dev'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path('.').absolute()/ 'instance' / 'xflask.db'}"
DEBUG = True