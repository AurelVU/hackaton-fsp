import marshmallow_dataclass

from app.models.contest_filters import ContestsFilters

ContestsFiltersSchema = marshmallow_dataclass.class_schema(ContestsFilters)
