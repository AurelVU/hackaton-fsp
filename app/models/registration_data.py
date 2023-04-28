from dataclasses import dataclass
from typing import Optional


@dataclass
class RegistrationData:
    name: str
    username: Optional[str]
    email: Optional[str]
    password: str
    type: str
    city_id: int
