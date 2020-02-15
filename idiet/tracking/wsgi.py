from .core import IDietTracker
from .api import api


def create_app():
    app = IDietTracker(__name__)
    app.register_blueprint(api)
    return app
