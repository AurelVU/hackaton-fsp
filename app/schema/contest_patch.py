import marshmallow_dataclass

from app.models.patch_contest import PatchContest

PatchContestSchema = marshmallow_dataclass.class_schema(PatchContest)
