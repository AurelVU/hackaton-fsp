import marshmallow_dataclass

from app.models import LoginData

LoginDataSchema = marshmallow_dataclass.class_schema(LoginData)
