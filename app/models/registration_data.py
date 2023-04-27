from dataclasses import dataclass


@dataclass
class RegistrationData:
    name: str
    username: str
    password: str
    type: str
    city_id: str
