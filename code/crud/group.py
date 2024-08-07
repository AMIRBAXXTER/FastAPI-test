from code.models.group import Group


async def create_group(db, group: Group):
    group_dict = group.dict(by_alias=True)
    result = await db["groups"].insert_one(group_dict)
    group_dict["_id"] = str(result.inserted_id)
    return group_dict

async def get_group(db, group_id):
    result = await db["groups"].find_one({"_id": group_id})
    return result
