from datetime import datetime
from typing import Optional, List
from beanie import Document, Indexed
from bson import ObjectId
from pydantic import Field


class User(Document):
    username: Indexed(str, unique=True) = Field(...)
    password: str


class Message(Document):
    sender_id: ObjectId = Field()
    receiver_id: Optional[ObjectId] = Field(None)
    group_id: Optional[ObjectId] = Field(None)
    content: Optional[str] = Field(None)
    file_url: Optional[str] = Field(None)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    def __repr__(self):
        return f"<Message(sender_id={self.sender_id}, receiver_id={self.receiver_id}, group_id={self.group_id}, content={self.content}, file_url={self.file_url})>"


class Group(Document):
    name: Indexed(str, unique=True) = Field(..., description="Group name is required and must be unique")
    description: Optional[str] = Field(None, description="Group description can be empty")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Time when the group was created")
    members: List[ObjectId] = Field(default_factory=list, description="List of member IDs")
    owner_id: ObjectId = Field(..., description="Owner ID is required")
