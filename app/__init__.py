from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api

from app.config import BaseConfig
from app.schema import UserSchema
from . import resource
from .models.init_db import db
from .resource.init_guard import guard
from .schema.init_ma import ma

cors = CORS()
migrate = Migrate()
api = Api(authorizations={
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    },
})

from .models import *


def create_app():
    config = BaseConfig  # Todo: fixme!!!

    app = Flask('backend-for-flutter-training-project')
    app.config.from_object(config)
    app.debug = True
    from app.models import User
    with app.app_context():
        guard.init_app(app, User)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    api.add_namespace(resource.user_ns)
    api.add_namespace(resource.team_ns)
    api.add_namespace(resource.contest_ns)
    # api.add_namespace(resource.post_ns)
    # api.add_namespace(resource.comment_ns)

    cors.init_app(app)

    return app