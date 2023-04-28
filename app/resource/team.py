from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace

from app.models import Invite
from app.models import User, Team
from app.models.init_db import db
from app.resource.init_guard import guard
from app.schema import UserSchema, RegistrationDataSchema, LoginDataSchema, EditProfileDataSchema, EditTeamDataSchema, \
    InviteSchema, InviteStatusDataSchema
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
class TeamResource(Resource):
    # просмотр команды со списком участников
    @team_ns.doc('Team data', security='Bearer')
    @responds(schema=TeamSchema, api=team_ns, status_code=200)
    def get(self, team_id):
        #todo
        return db.session.query(Team).get(team_id)

    @team_ns.doc('Team editing', security='Bearer')
    @accepts(schema=EditTeamDataSchema, api=team_ns)
    @responds(schema=TeamSchema, api=team_ns, status_code=200)
    def put(self, team_id):
        team_changed = request.parsed_obj
        team = Team.query.get(team_id)
        if team.owner_id != guard.extract_jwt_token(guard.read_token())['id']:
            return {'status': 'error', 'message': 'Permission denied'}, 403
        team.name = team_changed.name
        db.session.add(team)
        db.session.commit()
        return team


@team_ns.route("/invite/")
class InviteResource(Resource):
    @team_ns.doc("Invite")
    @accepts(schema=InviteSchema, api=team_ns)
    @responds(schema=None, api=team_ns, status_code=200)
    def post(self):
        data = request.parsed_obj
        db.session.add(data)
        db.session.commit()
        return {"status": "ok"}

    @team_ns.doc('Invites list', security='Bearer')
    @responds(schema=InviteSchema, api=team_ns, status_code=200, many=True)
    def get(self):
        return db.session.query(Invite).filter(
            Invite.user_id == guard.extract_jwt_token(guard.read_token())['id']).all()


@team_ns.route("/accept_invite")
class InviteAcceptResource(Resource):
    @team_ns.doc("AcceptInvite")
    @accepts(schema=InviteStatusDataSchema, api=team_ns)
    @responds(schema=None, api=team_ns, status_code=200)
    def post(self):
        data = request.parsed_obj
        invite = Invite.query.get(data.id)
        if data.status:
            user = User.query.get(invite.user_id)
            user.team_id = invite.team_id
            db.session.add(user)
        db.session.delete(invite)
        db.session.commit()
        return {"status": "ok"}


# @team_ns.route("/invite/")
# class ContestResource(Resource):
#     @team_ns.doc('Invites list', security='Bearer')
#     @responds(schema=InviteSchema, api=team_ns, status_code=200, many=True)
#     def get(self):
#         return db.session.query(Invite).filter(Invite.user_id == guard.extract_jwt_token(guard.read_token())['id']).all()
