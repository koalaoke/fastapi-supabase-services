from fastapi import UploadFile, HTTPException
from database import supabase
import uuid

async def upload_image(file: UploadFile, bucket: str, folder: str) -> str:
    """
    Função genérica que valida e envia imagem para o Supabase.
    Retorna a URL pública.
    """
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(400, "Apenas JPG ou PNG são permitidos.")
    
    file_ext = file.filename.split(".")[-1]
    file_path = f"{folder}/{uuid.uuid4()}.{file_ext}"
    file_content = await file.read()

    try:
        supabase.storage.from_(bucket).upload(
            file=file_content,
            path=file_path,
            file_options={"content-type": file.content_type}
        )
        return supabase.storage.from_(bucket).get_public_url(file_path)
    
    except Exception as e:
        raise HTTPException(400, f"Erro no upload: {str(e)}")
    