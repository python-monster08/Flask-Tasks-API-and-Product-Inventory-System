from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # To allow cross-origin requests (if needed)
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("app.config.Config")

    # Initialize the database with the app
    db.init_app(app)

    # Enable CORS for all routes
    CORS(app)

    # Set up logging to display incoming requests and errors for easier debugging
    logging.basicConfig(level=logging.INFO)

    # Register the blueprint for task routes
    from .routes import tasks_bp
    app.register_blueprint(tasks_bp)

    # Log the app start message
    logging.info("Flask app started and database initialized")

    return app
