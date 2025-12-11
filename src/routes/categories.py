from fastapi import APIRouter
from src.schemas.categories import CategoryModel, UpdateCategoryModel
from src.database import supabase

router = APIRouter()

@router.post("/categories")
async def create_category(category : CategoryModel):
    supabase.table("categories").insert(category.model_dump()).execute()
    return category

@router.get("/categories")
async def get_categories():
    categories = supabase.table("categories").select("*").execute()
    return categories

@router.patch("/categories/{category_id}")
async def update_category(category_id : str , updated_category : UpdateCategoryModel):
    supabase.table("categories").update(updated_category.model_dump()).eq("id",category_id).execute()
    return updated_category

@router.delete("/categories/{category_id}")
async def delete_category(category_id : str):
    supabase.table("categories").delete().eq("id",category_id).execute()
    return "Operação feita"
