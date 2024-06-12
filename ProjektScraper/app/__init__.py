import os
from flask import Flask
from flask_pymongo import PyMongo
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

mongo = PyMongo()


def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.getenv("MONGO_URI","mongodb+srv://Python1:VI9Mb3hDJoDn4nb4@python.0c7bytz.mongodb.net/python_db")

    try:
        mongo.init_app(app)
        logger.debug("MongoDB connected successfully")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")

    from .routes import main
    app.register_blueprint(main)

    return app
