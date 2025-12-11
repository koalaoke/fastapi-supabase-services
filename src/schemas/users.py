from pydantic import BaseModel

class UserModel(BaseModel):
    email : str
    password : str

class UpdateUserModel(UserModel):
    email: str | None = None
    password: str | None = None
