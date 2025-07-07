import logging
from logging.handlers import RotatingFileHandler

def configure_logging(app):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    
    file_handler = RotatingFileHandler(
        app.config['LOG_FILE'], maxBytes=10240, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)