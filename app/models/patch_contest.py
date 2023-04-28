from dataclasses import dataclass
from typing import Optional


@dataclass
class PatchContest:
    active: Optional[bool]
