from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource, Namespace

from app.models import User
from app.models.init_db import db
from app.resource.init_guard import guard
from app.schema import UserSchema, RegistrationDataSchema, LoginDataSchema, EditProfileDataSchema
from app.schema.login import LoginDataSchema

user_ns = Namespace('user', description='Операции для взаимодействия с пользователями')


@user_ns.route("/login")
class UserLoginResource(Resource):
    @user_ns.doc('Login')
    @accepts(schema=LoginDataSchema, api=user_ns)
    def post(self):
        data = request.parsed_obj
        username = data.username or data.email
        user = guard.authenticate(username, data.password)
        return {"access_token": guard.encode_jwt_token(user), 'id': user.id}


@user_ns.route("/registration")
class UserRegistrationResource(Resource):
    @user_ns.doc('Registration')
    @accepts(schema=RegistrationDataSchema, api=user_ns)
    @responds(schema=None, api=user_ns, status_code=200)
    def post(self):
        data = request.parsed_obj
        user = User(
            name=data.name,
            username=data.username,
            hashed_password=guard.hash_password(data.password),
            city_id=data.city_id,
            type=data.type
        )
        db.session.add(user)
        db.session.commit()
        return {'status': 'ok'}


@user_ns.route("/<int:user_id>")
class UserResource(Resource):
    @user_ns.doc('User data', security='Bearer')
    @responds(schema=UserSchema, api=user_ns, status_code=200)
    def get(self, user_id):
        return db.session.query(User).get(user_id)

    @user_ns.doc('User editing', security='Bearer')
    @accepts(schema=EditProfileDataSchema, api=user_ns)
    @responds(schema=UserSchema, api=user_ns, status_code=200)
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