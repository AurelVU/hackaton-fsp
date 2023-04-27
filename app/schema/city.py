from .init_ma import ma
from ..models.city import City


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        load_instance = True
