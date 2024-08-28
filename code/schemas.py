from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str


class Message(BaseModel):
    id: str
    sender_id: str
    receiver_id: Optional[str] = None
    group_id: Optional[str] = None
    content: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    timestamp: datetime


class Group(BaseModel):
    id: str
    name: str
    members: List[str]
