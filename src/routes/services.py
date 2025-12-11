from fastapi import APIRouter
from src.schemas.services import ServiceModel, UpdateServiceModel
from src.database import supabase

router = APIRouter()

@router.post("/services")
async def create_service(service : ServiceModel):
    supabase.table("services").insert(service.model_dump()).execute()
    return service

@router.get("/services")
async def get_services():
    services = supabase.table("services").select("*").execute()
    return services

@router.patch("/services/{service_id}")
async def update_service(service_id : str , updated_service : UpdateServiceModel):
    supabase.table("services").update(updated_service.model_dump()).eq("id",service_id).execute()
    return updated_service

@router.delete("/services/{service_id}")
async def delete_service(service_id : str):
    supabase.table("services").delete().eq("id",service_id).execute()
    return "Operação feita"
