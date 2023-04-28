import marshmallow_dataclass

from app.models.rating_filters import RatingFilters

RatingFiltersSchema = marshmallow_dataclass.class_schema(RatingFilters)
