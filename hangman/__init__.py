# __init__.py
import os
from flask import Flask
from .models import db
from .routes import configure_routes

def create_app():
    app = Flask(__name__)

    # Check if env.py file exists
    env_file_path = os.path.join(os.path.dirname(__file__), 'env.py')
    if os.path.exists(env_file_path):
        app.config.from_pyfile('env.py')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    configure_routes(app)

    return app
