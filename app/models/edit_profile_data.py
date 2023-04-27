from dataclasses import dataclass


@dataclass
class EditProfileData:
    name: str
    city_id: int
