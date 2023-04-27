import enum

from sqlalchemy import Enum

from .init_db import db


class ContestType(enum.Enum):
    individual = 0,
    command = 1,


class ContestFormat(enum.Enum):
    task_based = 0,
    another = 1,


class Contest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(1024))
    datetime_start = db.Column(db.DateTime)
    datetime_end = db.Column(db.DateTime)
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    format = db.Column(Enum(ContestFormat))
    feeding = db.Column(db.Boolean)
    difficulty = db.Column(db.Integer)
    type = db.Column(Enum(ContestType))
    active = db.Column(db.Boolean)
    employer = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(50))
    organizer = db.relationship("User")
    city = db.relationship("City", backref='contests')

    # participants = models.ManyToManyField("UserModel", through='ContestParticipantThroughModel')
