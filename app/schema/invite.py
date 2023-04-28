from marshmallow_sqlalchemy import auto_field, fields

from .init_ma import ma
from ..models import Invite


class InviteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Invite
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)