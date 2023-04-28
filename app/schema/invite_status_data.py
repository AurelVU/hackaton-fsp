import marshmallow_dataclass
from marshmallow_sqlalchemy import auto_field, fields

from .init_ma import ma
from ..models import InviteStatusData


InviteStatusDataSchema = marshmallow_dataclass.class_schema(InviteStatusData)