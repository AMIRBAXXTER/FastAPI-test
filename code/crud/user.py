from code.models.user import User


async def create_user(db, user: User):
    user_dict = user.dict(by_alias=True)
    result = await db["users"].insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict


async def get_user(db, user_id: str):
    user = await db["users"].find_one({"_id": user_id})
    return user


async def authenticate_user(db, user_id: str, password: str):
    user = await get_user(db, user_id)
    if user.get("password") == password:
        return user
    return None
