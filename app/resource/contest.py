from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace

from app.models import Contest
from app.models.init_db import db
from app.resource.init_guard import guard
from app.schema import ContestSchema, ContestsFiltersSchema
# from app.schema.edit_profile_data import EditProfileDataSchema
from app.schema.login import LoginDataSchema

contest_ns = Namespace('contest', description='Операции для взаимодействия с контестами')


@contest_ns.route("/")
class CreationContestResource(Resource):
    @contest_ns.doc('Contest list')
    @accepts(query_params_schema=ContestsFiltersSchema, api=contest_ns)
    @responds(schema=ContestSchema, api=contest_ns, status_code=200, many=True)
    def get(self):
        data = request.parsed_query_params.__dict__
        data = {k: v for k, v in data.items() if v is not None}
        return db.session.query(Contest).filter_by(**data).all()

    @contest_ns.doc('Contest creation')
    @accepts(schema=ContestSchema, api=contest_ns)
    @responds(schema=ContestSchema, api=contest_ns, status_code=200)
    def post(self):
        data = request.parsed_obj
        contest = Contest(
            name=data.name,
            description=data.description,
            datetime_start=data.datetime_start,
            datetime_end=data.datetime_end,
            organizer_id=data.organizer_id,
            city_id=data.city_id,
            format=data.format,
            feeding=data.feeding,
            difficulty=data.difficulty,
            type=data.type,
            active=data.active,
            employer=data.employer,
            image_path=data.image_path,
        )
        db.session.add(contest)
        db.session.commit()
        return {'status': 'ok'}


@contest_ns.route("/<int:contest_id>")
class ContestResource(Resource):
    @contest_ns.doc('Contest data', security='Bearer')
    @responds(schema=ContestSchema, api=contest_ns, status_code=200)
    def get(self, contest_id):
        return db.session.query(Contest).get(contest_id)

    @contest_ns.doc('Contest editing', security='Bearer')
    @accepts(schema=ContestSchema, api=contest_ns)
    @responds(schema=ContestSchema, api=contest_ns, status_code=200)
    def put(self, contest_id):
        contest = request.parsed_obj
        # if contest_id != guard.extract_jwt_token(guard.read_token())['id']:  # ???
        #     return {'status': 'error', 'message': 'Permission denied'}, 403
        ccontest = Contest.query.get(contest_id)
        ccontest.description = contest.description
        ccontest.image_path = contest.image_path
        ccontest.difficulty = contest.difficulty
        ccontest.organizer_id = contest.organizer_id
        ccontest.datetime_start = contest.datetime_start
        ccontest.active = contest.active
        ccontest.feeding = contest.feeding
        ccontest.city_id = contest.city_id
        ccontest.name = contest.name
        ccontest.employer = contest.employer
        ccontest.datetime_end = contest.datetime_end
        db.session.add(ccontest)
        db.session.commit()
        return contest

    @contest_ns.doc('Contest delete', security='Bearer')
    # @responds(schema=UserSchema, api=user_ns, status_code=200)
    def delete(self, contest_id):
        contest = db.session.query(Contest).get(contest_id)
        db.session.delete(contest)
        db.session.commit()
        return {'status': 'ok'}
