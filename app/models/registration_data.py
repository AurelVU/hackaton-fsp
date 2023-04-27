from dataclasses import dataclass


@dataclass
class RegistrationData:
    nickname: str
    firstname: str
    lastname: str
    password: str
    website: str
