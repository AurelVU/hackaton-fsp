import marshmallow_dataclass

from ..resource import LoginData

LoginDataSchema = marshmallow_dataclass.class_schema(LoginData)
