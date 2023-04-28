import enum

from sqlalchemy import Enum

from .init_db import db
from .city import City


class Type(enum.Enum):
    sportsman = 0,
    partner = 1,
    regional = 2,
    admin = 3


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Integer, default=0)
    hashed_password = db.Column(db.String(255))
    type = db.Column(Enum(Type))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    team = db.relationship('Team', backref='members', primaryjoin='User.team_id == Team.id')

    @property
    def identity(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has an ``identity`` instance
        attribute or property that provides the unique id of the user instance
        """
        return self.id

    @property
    def rolenames(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has a ``rolenames`` instance
        attribute or property that provides a list of strings that describe the roles
        attached to the user instance
        """
        try:
            return ['user']
        except Exception:
            return []

    @property
    def password(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has a ``password`` instance
        attribute or property that provides the hashed password assigned to the user
        instance
        """
        return self.hashed_password

    @classmethod
    def lookup(cls, email):
        """
        *Required Method*
        flask-praetorian requires that the user class implements a ``lookup()``
        class method that takes a single ``username`` argument and returns a user
        instance if there is one that matches or ``None`` if there is not.
        """
        return db.session.query(cls).filter_by(email=email).first()

    @classmethod
    def identify(cls, user_id):
        """
        *Required Method*
        flask-praetorian requires that the user class implements an ``identify()``
        class method that takes a single ``id`` argument and returns user instance if
        there is one that matches or ``None`` if there is not.
        """
        return db.session.query(cls).get(user_id)
