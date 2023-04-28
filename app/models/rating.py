from dataclasses import dataclass


@dataclass
class Rating:
    name: str
    nickname: str
    rating: int
    city: str

