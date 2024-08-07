from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Message(BaseModel):
    id: str
    sender_id: str
    receiver_id: Optional[str] = None
    group_id: Optional[str] = None
    content: Optional[str] = None
    file_url: Optional[str] = None
    file_type: Optional[str] = None
    timestamp: datetime
