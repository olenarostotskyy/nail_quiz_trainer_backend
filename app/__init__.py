from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SLACK_TOKEN"]=os.environ.get("SLACK_TOKEN")

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.quiz import Quiz
    from app.models.user import User
    from app.models.card import Card
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes.quiz import questions_bp
    app.register_blueprint(questions_bp)

    from .routes.user import users_bp
    app.register_blueprint(users_bp)

    from .routes.card import cards_bp
    app.register_blueprint(cards_bp)

    CORS(app)
    return app
