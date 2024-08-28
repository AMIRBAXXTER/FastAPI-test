from code.models import User
from fastapi import HTTPException
from utils.password_handling import set_password, check_password


async def create_user(db, username: str, password: str):
    user = db.users.find_one({"username": username})
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    user_dict = User(username=username, password=set_password(password)).dict(by_alias=True)
    result = await db["users"].insert_one(user_dict)
    return result


async def delete_user(db, username: str, password: str):
    user = db.users.find_one({"username": username})
    if not user or not check_password(password) == user['password']:
        return False
    await db["users"].delete_one({"username": username})
    return True


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


async def create_group(db, group: Group):
    group_dict = group.dict(by_alias=True)
    result = await db["groups"].insert_one(group_dict)
    group_dict["_id"] = str(result.inserted_id)
    return group_dict


async def get_group(db, group_id):
    result = await db["groups"].find_one({"_id": group_id})
    return result
