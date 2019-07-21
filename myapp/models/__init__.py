# project/models/__init__.py


def init_app(app):
    from .base import a
    a.init_app(app)
