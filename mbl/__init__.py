"""
    App factory module
"""


from flask import Flask

from config import config
from .api.routes import v1


def create_app(config_name):
    """
    Usage: Factory function used to setup the application instance
    :return: application instance
    """
    app = Flask(__name__, template_folder='../api_docs')
    app.database = DATABASE
    app.config.from_object(config[config_name])
    app.config['BUNDLE_ERRORS'] = True

    @app.route('/')
    def api_docs():
        """ Route to the api docs"""
        from flask import render_template
        return render_template('api.html')
    # Register Blueprint here
    app.register_blueprint(v1, url_prefix="/api")

    return app
