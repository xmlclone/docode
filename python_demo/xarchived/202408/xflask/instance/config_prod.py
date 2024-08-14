import secrets
from pathlib import Path


SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path('.').absolute()/ 'instance' / 'xctools.db'}"
DEBUG = False
# # python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = secrets.token_hex()