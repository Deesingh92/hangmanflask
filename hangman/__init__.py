from flask import Flask
from .models import db
from .routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('env.py')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    configure_routes(app)

    return app