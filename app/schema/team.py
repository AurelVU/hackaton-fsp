from marshmallow_sqlalchemy import auto_field, fields

from .init_ma import ma
from .. import UserSchema
from ..models import Team


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)
    members = fields.Nested(UserSchema, dump_only=True, many=True)
