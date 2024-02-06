import os
from flask import Flask
from .db import db, migrate
from .model import cat
from .model import caregiver
from .route import cats

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cats.bp)

    return app
