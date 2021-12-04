# -*- coding: utf-8 -*-
#########################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from config import Config


def create_app():
    from.api_v1 import api as api_blueprint

    app.config.from_object(Config())
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_blueprint, url_prefix='/api/v1')


# SQLAlchemy
db = SQLAlchemy()
ma = Marshmallow()

# Flask Migrate
migrate = Migrate()

# Flask
app = Flask(__name__)
create_app()
