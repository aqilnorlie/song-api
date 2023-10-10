from flask import Flask
import os
from extension import db

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("secret_key")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # location db and name db
    db.init_app(app)

    return app
