from marshmallow import fields
from marshmallow.fields import Nested
from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import auto_field

from .city import CitySchema
from app.models import User
from app.models.user import Type
from .city import CitySchema

from app.schema.init_ma import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = False
        include_relationships = True

    id = auto_field(dump_only=True)
    name = auto_field()
    username = auto_field()
    email = auto_field()
    rating = auto_field()
    hashed_password = auto_field(load_only=True)
    is_activated = auto_field()
    type = EnumField(Type, by_value=True)
    city = ma.Nested(CitySchema(only=("name",)))
    city_id = fields.String(attribute="city.name")
    team_id = auto_field()  # Добавьте поле внешнего ключа, которое вы хотите сериализовать
