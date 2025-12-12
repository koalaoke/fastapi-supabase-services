from fastapi import APIRouter, UploadFile
from src.schemas.services import ServiceModel, UpdateServiceModel
from src.database import supabase
from src.utils.storage import upload_image, delete_image_from_url

router = APIRouter(prefix="/services")

@router.post("")
async def create_service(service : ServiceModel):
    supabase.table("services").insert(service.model_dump()).execute()
    return service

@router.get("")
async def get_services():
    services = supabase.table("services").select("*").execute()
    return services

@router.patch("/{service_id}")
async def update_service(service_id : str , updated_service : UpdateServiceModel):
    supabase.table("services").update(updated_service.model_dump()).eq("id",service_id).execute()
    return updated_service

@router.delete("/{service_id}")
async def delete_service(service_id : str):
    supabase.table("services").delete().eq("id",service_id).execute()
    return "Operação feita"

@router.post("/{service_id}/logo")
async def upload_logo(service_id : str, file : UploadFile):
    response = supabase.table("services").select("*").eq("id",service_id).execute()
    service = response.data[0]
    if service.get("logo_url") is not None:
        await delete_image_from_url(service.get("logo_url"),"avatars")
    public_url = await upload_image(file, "avatars", "services")
    supabase.table("services").update({"logo_url" : public_url}).eq("id",service_id).execute()
    return {"message": "Logo atualizada", "url": public_url} 
        
@router.delete("/{service_id}/logo",status_code=204)
async def delete_logo(service_id : str):
    response = supabase.table("services").select("*").eq("id",service_id).execute()
    service = response.data[0]
    await delete_image_from_url(service.get("logo_url"),"avatars")
    supabase.table("services").update({"logo_url" : None}).eq("id",service_id).execute()