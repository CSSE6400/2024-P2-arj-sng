from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(config_overrides=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    if config_overrides:
        app.config.update(config_overrides)

    # Load models
    from todo.models import db
    from todo.models.todo import Todo
    db.init_app(app)

    # Make tables
    with app.app_context():
        db.create_all()
        db.session.commit()

    # blueprints
    from .views.routes import api
    app.register_blueprint(api)

    return app
