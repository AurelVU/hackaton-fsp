from marshmallow_sqlalchemy import auto_field

from .init_ma import ma
from ..models import Team


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        load_instance = True

    id = auto_field(dump_only=True)