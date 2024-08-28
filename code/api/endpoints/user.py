from fastapi import APIRouter, HTTPException
from code.schemas import User
from code.crud import create_user, delete_user
from code.database import mongodb
from code.utils.password_handling import check_password

router = APIRouter()


@router.post("/create-user/", response_model=User)
async def create_new_user(username: str, password: str):
    user = await create_user(mongodb.db, username, password)
    return user


@router.post("/delete-user/")
async def delete_user(username: str, password: str):
    result = await delete_user(mongodb.db, username, password)
    if result:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found or password not correct")


@router.post("/login/")
async def login(username: str, password: str):
    user = await mongodb.db.users.find_one({"username": username, "password": check_password(password)})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found or password not correct")
