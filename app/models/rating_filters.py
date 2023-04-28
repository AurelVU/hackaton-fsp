from dataclasses import dataclass
from typing import Optional


@dataclass
class RatingFilters:
    city_id: Optional[int]
    username: Optional[str]
