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
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes.quiz import questions_bp
    app.register_blueprint(questions_bp)

    CORS(app)
    return app


# from flask import Flask

# def create_app(test_config=None):
#     app = Flask(__name__)
    
#     # from app.models.quiz import Quiz

#     from .routes.quiz import questions_bp
#     app.register_blueprint(questions_bp)

#     return app