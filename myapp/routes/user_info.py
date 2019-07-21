from flask import Blueprint
from flask import jsonify
import traceback

bp_user = Blueprint('api', __name__)
logger = None

print('user_info: import')
a = 10

def init_app(app):
    global logger
    app.register_blueprint(bp_user)
    logger = app.logger

@bp_user.route('/hello/<name>', methods=['GET'])
def hello(name):
    try:
        logger.warn("success invoke")
        return jsonify({
            "result": "hello, %s!" % name
        })
    except Exception as e:
        logger.warn("error: %s" % traceback.format_exc())
        return jsonify({"result": None, "error": "%s" % e})

