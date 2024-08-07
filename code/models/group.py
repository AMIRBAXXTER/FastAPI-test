from pydantic import BaseModel
from typing import List


class Group(BaseModel):
    id: str
    name: str
    members: List[str]
