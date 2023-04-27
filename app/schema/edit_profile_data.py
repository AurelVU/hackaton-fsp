import marshmallow_dataclass

from app.models import EditProfileData

EditProfileDataSchema = marshmallow_dataclass.class_schema(EditProfileData)
