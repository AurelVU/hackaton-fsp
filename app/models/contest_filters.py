from dataclasses import dataclass
from typing import Optional


@dataclass
class ContestsFilters:
    datetime_start: Optional[str]
    datetime_end: Optional[str]
    city: Optional[int]
    format: Optional[int]
    feeding: Optional[bool]
    difficulty: Optional[int]
    type: Optional[int]
