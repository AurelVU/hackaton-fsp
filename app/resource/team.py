from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace

from app.models import User, Team
from app.models.init_db import db
from app.resource.init_guard import guard
from app.schema import UserSchema, RegistrationDataSchema, LoginDataSchema, EditProfileDataSchema
from app.schema.login import LoginDataSchema
from app.schema.team import TeamSchema

team_ns = Namespace('team', description='Операции для взаимодействия с пользователями')


@team_ns.route("/")
class TeamResource(Resource):
    @team_ns.doc('Team')
    @accepts(schema=TeamSchema, api=team_ns)
    @responds(schema=None, api=team_ns, status_code=200)
    def post(self):
        data = request.parsed_obj
        db.session.add(data)
        db.session.commit()
        return {'status': 'ok'}


@team_ns.route("/<int:team_id>")
class UserResource(Resource):
    # просмотр команды со списком участников
    @team_ns.doc('Team data', security='Bearer')
    @responds(schema=TeamSchema, api=team_ns, status_code=200)
    def get(self, team_id):
        #todo
        return db.session.query(Team).get(team_id)

    @team_ns.doc('User editing', security='Bearer')
    @accepts(schema=EditProfileDataSchema, api=team_ns)
    @responds(schema=UserSchema, api=team_ns, status_code=200)
    def put(self, user_id):
        user = request.parsed_obj
        if user_id != guard.extract_jwt_token(guard.read_token())['id']:
            return {'status': 'error', 'message': 'Permission denied'}, 403
        cuser = User.query.get(user_id)
        cuser.firstname = user.firstname
        cuser.lastname = user.lastname
        cuser.website = user.website
        db.session.add(cuser)
        db.session.commit()
        return user