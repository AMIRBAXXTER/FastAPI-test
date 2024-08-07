from typing import List
from fastapi import APIRouter, Depends, HTTPException
from code.models.message import Message
from code.crud.message import create_message, get_private_messages, get_group_messages
from code.db.database import mongodb

router = APIRouter()


@router.post("/messages/", response_model=Message)
async def send_message(message: Message):
    message = await create_message(mongodb.db, message)
    return message


@router.get("/messages/{user_id}", response_model=List[Message])
async def get_user_messages(user_id: str):
    messages = await get_private_messages(mongodb.db, user_id)
    if not messages:
        raise HTTPException(status_code=404, detail="No messages found")
    return messages


@router.get("/groups/{group_id}/messages", response_model=List[Message])
async def get_group_messages(group_id: str):
    messages = await get_group_messages(mongodb.db, group_id)
    if not messages:
        raise HTTPException(status_code=404, detail="No messages found")
    return messages
