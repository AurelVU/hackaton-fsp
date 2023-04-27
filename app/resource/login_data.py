from dataclasses import dataclass


@dataclass
class LoginData:
    email: str
    password: str
