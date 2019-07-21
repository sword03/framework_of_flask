'''
Log module
usage:

logger_me.error('error')
logger_me.warn('warning')
logger_me.log('log')
logger_me.debug('debug')
'''

import logging
from logging.handlers import RotatingFileHandler
import os
import sys


def init_app(app):
    # Check the param: LOG_LEVEL，exit the program if invalid
    numeric_level = getattr(logging, app.config['LOG_LEVEL'].upper(), None)
    if not isinstance(numeric_level, int):
        app.logger.error('Invalid log level: %s' % numeric_level)
        sys.exit(0)

    dir = os.path.dirname(app.config['LOG_PATH'])
    # Create the directory to store the log files
    if not os.path.exists(dir):
        os.makedirs(dir)

    # Set log level
    app.logger.setLevel(app.config['LOG_LEVEL'])

    # Create a file handler
    fh = RotatingFileHandler(app.config['LOG_PATH'])
    fh.setLevel(app.config['LOG_LEVEL'])
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add a file handle to the flask logger
    # app.logger.addHandler(fh)
    # Add a file handle to the root logger
    root = logging.getLogger()
    root.addHandler(fh)
