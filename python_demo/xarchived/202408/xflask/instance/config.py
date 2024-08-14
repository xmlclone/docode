from pathlib import Path


SECRET_KEY = 'default'
SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path('.').absolute()/ 'instance' / 'xctools.db'}"