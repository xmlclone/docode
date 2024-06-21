from pathlib import Path


SECRET_KEY = 'test'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path('.').absolute()/ 'instance' / 'xctools.db'}"
DEBUG = True