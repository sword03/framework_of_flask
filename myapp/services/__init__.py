# project/services/__init__.py
from . import log


def init_app(app):
    log.init_app(app)
