from pydantic import BaseModel

class ServiceModel(BaseModel):
    name : str
    city_id : str
    category_id : str

class UpdateServiceModel(ServiceModel):
    name : str | None = None 
    city_id : str | None = None
    category_id : str | None = None
