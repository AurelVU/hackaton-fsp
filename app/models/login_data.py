from dataclasses import dataclass
from typing import Optional


@dataclass
class LoginData:
    email: Optional[str]
    username: Optional[str]
    password: str
