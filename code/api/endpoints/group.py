from fastapi import APIRouter, Depends, HTTPException
from code.models.group import Group
from code.crud.group import create_group, get_group
from code.db.database import mongodb

router = APIRouter()


@router.post("/groups/", response_model=Group)
async def create_new_group(group: Group):
    group = await create_group(mongodb.db, group)
    return group


@router.get("/groups/{group_id}", response_model=Group)
async def read_group(group_id: str):
    group = await get_group(mongodb.db, group_id)
    if group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return group
