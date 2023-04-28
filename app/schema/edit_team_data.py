import marshmallow_dataclass

from app.models import EditTeamData

EditTeamDataSchema = marshmallow_dataclass.class_schema(EditTeamData)
