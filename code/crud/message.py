from code.models.message import Message


async def create_message(db, message: Message):
    message_dict = message.dict(by_alias=True)
    result = await db["messages"].insert_one(message_dict)
    message_dict["_id"] = str(result.inserted_id)
    return message_dict


async def get_private_messages(db, user_id: str, receiver_id: str):
    user_messages = await db["messages"].find({"user_id": user_id, "receiver_id": receiver_id}).to_list(None)
    receiver_messages = await db["messages"].find({"user_id": receiver_id, "receiver_id": user_id}).to_list(None)
    messages = user_messages + receiver_messages
    return messages


async def get_group_messages(db, group_id: str):
    messages = await db["messages"].find({"group_id": group_id}).to_list(None)
    return messages
