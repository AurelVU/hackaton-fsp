from marshmallow.fields import Nested
from marshmallow_sqlalchemy import auto_field

from app.models import User

from app.schema.init_ma import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)
    hashed_password = auto_field(load_only=True)
    avatar_url = auto_field(load_default=None)