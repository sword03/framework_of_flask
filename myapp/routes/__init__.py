print('routes: __init__')


def init_app(app):
    from . import user_info
    user_info.init_app(app)
