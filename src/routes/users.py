from fastapi import APIRouter
from src.database import supabase
from src.schemas.users import UserModel, UpdateUserModel

router = APIRouter()

@router.get("/users")
async def get_users(skip : int = 0, limit : int = 10):
    users = supabase.auth.admin.list_users()
    return users[skip : skip + limit]

@router.post("/users")
async def create_users(user : UserModel):
    supabase.auth.admin.create_user(user.model_dump())
    return user.model_dump()

@router.get("/users/{user_id}")
async def get_user(user_id : str):
    user = supabase.auth.admin.get_user_by_id(user_id)
    return user

@router.patch("/users/{user_id}")
async def update_user(user_id : str, update_user : UpdateUserModel):
    update_data = update_user.model_dump(exclude_unset=True)
    supabase.auth.admin.update_user_by_id(user_id,update_data)
    return update_user