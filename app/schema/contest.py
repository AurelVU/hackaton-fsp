from marshmallow_sqlalchemy import auto_field

from app.models import Contest

from app.schema.init_ma import ma


class ContestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contest
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)
    organizer_id = auto_field(load_only=True)
    organizer = auto_field(dump_only=True)

    # name = db.Column(db.String(50))
    # description = db.Column(db.String(1024))
    # datetime_start = db.Column(db.DateTime)
    # datetime_end = db.Column(db.DateTime)
    # organizer = db.Column(db.Integer, db.ForeignKey('organizer.id'), nullable=False)
    # city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    # format = db.Column(Enum(ContestFormat))
    # feeding = db.Column(db.Boolean)
    # difficulty = db.Column(db.Integer)
    # type = db.Column(Enum(ContestType))
    # active = db.Column(db.Boolean)
    # employer = db.Column(db.String(50), nullable=False)
    # image_path = db.Column(db.String(50))

