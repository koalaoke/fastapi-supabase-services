from pydantic import BaseModel

class UserModel(BaseModel):
    email : str
    password : str
    avatar_url : str | None = None

class UpdateUserModel(UserModel):
    email: str | None = None
    password: str | None = None
