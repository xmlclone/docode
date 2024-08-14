from pathlib import Path


SECRET_KEY = 'dev'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path('.').absolute()/ 'instance' / 'xctools.db'}"
DEBUG = True