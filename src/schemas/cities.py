from pydantic import BaseModel

class CityBase(BaseModel):
    name : str

class UpdateCityModel(CityBase):
    name : str | None = None