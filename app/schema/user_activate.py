import marshmallow_dataclass

from ..models import UserActivateData

UserActivateDataSchema = marshmallow_dataclass.class_schema(UserActivateData)
