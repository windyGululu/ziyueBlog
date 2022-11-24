import imp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .db_config import db_config
from .global_params import db
from apps.user.user_view import user


def create_app():
    app = Flask(__name__)
    app.config.from_object(db_config)
    db.init_app(app)
    register_blueprints(app)

    return app
    

def register_blueprints(app):
    # 注册蓝图
    app.register_blueprint(user)