from fastapi import APIRouter, Depends, HTTPException
from code.models.user import User
from code.crud.user import create_user, get_user
from code.db.database import mongodb

router = APIRouter()


@router.post("/users/", response_model=User)
async def create_new_user(user: User):
    user = await create_user(mongodb.db, user)
    return user


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await get_user(mongodb.db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
