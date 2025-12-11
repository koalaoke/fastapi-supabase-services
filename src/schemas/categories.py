from pydantic import BaseModel

class CategoryModel(BaseModel):
    name : str

class UpdateCategoryModel(CategoryModel):
    name: str | None = None