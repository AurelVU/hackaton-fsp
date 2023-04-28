import marshmallow_dataclass

from app.models.rating import Rating

RatingSchema = marshmallow_dataclass.class_schema(Rating)
