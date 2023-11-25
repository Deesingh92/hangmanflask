# hangman/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Create the Flask app
app = Flask(__name__)

# Load configuration from env.py or environment variables
app.config.from_pyfile('env.py', silent=True)

# Configure the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URL", "postgresql:///hangman")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Import routes to ensure they are registered with Flask
from . import routes

# Import models to ensure they are registered with SQLAlchemy
from .models import HangmanWord

# Create tables if not exists
with app.app_context():
    db.create_all()

# Register routes with the app
routes.configure_routes(app)
