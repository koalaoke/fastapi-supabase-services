from fastapi import APIRouter
from src.schemas.cities import CityBase, UpdateCityModel
from src.database import supabase

router = APIRouter()

@router.post("/cities")
async def create_city(city : CityBase):
    supabase.table("cities").insert({"name" : city.name}).execute()
    return city

@router.get("/cities")
async def get_cities():
    cities = supabase.table("cities").select("*").execute()
    return cities

@router.patch("/cities/{city_id}")
async def update_city(city_id : str , updated_city : UpdateCityModel):
    supabase.table("cities").update(updated_city.model_dump()).eq("id",city_id).execute()
    return updated_city

@router.delete("/cities/{city_id}")
async def delete_city(city_id : str):
    supabase.table("cities").delete().eq("id",city_id).execute()
    return "Operação feita"
