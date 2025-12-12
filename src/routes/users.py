from fastapi import APIRouter, UploadFile
from src.database import supabase
from src.schemas.users import UserModel, UpdateUserModel
from src.utils.storage import upload_image, delete_image_from_url

router = APIRouter(prefix="/users")

@router.get("")
async def get_users(skip : int = 0, limit : int = 10):
    users = supabase.auth.admin.list_users()
    return users[skip : skip + limit]

@router.post("")
async def create_users(user : UserModel):
    response = supabase.auth.admin.create_user({
        "email" : user.email,
        "password" : user.password,
        "email_confirm" : True
    })
    return response

@router.get("/{user_id}")
async def get_user(user_id : str):
    user = supabase.auth.admin.get_user_by_id(user_id)
    return user

@router.patch("/{user_id}")
async def update_user(user_id : str, update_user : UpdateUserModel):
    update_data = update_user.model_dump(exclude_unset=True)
    response = supabase.auth.admin.update_user_by_id(user_id,update_data)
    return response

@router.post("/{user_id}/avatar")
async def upload_avatar(user_id: str, file: UploadFile):
    user_obj = supabase.auth.admin.get_user_by_id(user_id)
    if user_obj.user.user_metadata.get("avatar_url") is not None:
        await delete_image_from_url(user_obj.user.user_metadata["avatar_url"],"avatars")
    public_url = await upload_image(file=file,bucket="avatars",folder="users")
    supabase.auth.admin.update_user_by_id(user_id,{"user_metadata": {"avatar_url": public_url}})
    return {"message": "Avatar atualizado", "url": public_url} 

@router.delete("/{user_id}/avatar",status_code=204)
async def delete_avatar(user_id: str):
    response = supabase.auth.admin.get_user_by_id(user_id)
    avatar_url : str = response.user.user_metadata.get("avatar_url")
    await delete_image_from_url(avatar_url,"avatars")
    supabase.auth.admin.update_user_by_id(
        user_id,
        {"user_metadata" : {
            "avatar_url" : None
        }}
        )
