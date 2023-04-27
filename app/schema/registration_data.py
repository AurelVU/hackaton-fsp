import marshmallow_dataclass

from app.models.registration_data import RegistrationData

RegistrationDataSchema = marshmallow_dataclass.class_schema(RegistrationData)
