import os
from flask import Flask


def create_app():
    from . import services
    from . import routes
    app = Flask(__name__, instance_relative_config=True)
    # load default common configuration
    app.config.from_object('config.default')
    # load default configuration of instance
    if os.path.exists(os.getcwd() + 'default.py'):
        app.config.from_pyfile('default.py')  # 从instance文件夹中加载配置
    app.config.from_pyfile('default.py')
    # load specified common configuration
    if 'FLASK_COMMON_CONF' in os.environ:
        app.config.from_envvar('FLASK_COMMON_CONF')
    # load specified configuration of instance
    if 'FLASK_INSTANCE_CONF' in os.environ:
        app.config.from_envvar('FLASK_INSTANCE_CONF')

    routes.init_app(app)
    services.init_app(app)
    return app
