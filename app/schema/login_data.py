import marshmallow_dataclass

from app.models.login_data import LoginData

LoginDataSchema = marshmallow_dataclass.class_schema(LoginData)
