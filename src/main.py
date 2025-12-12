from fastapi import FastAPI
from src.routes.users import router as users_router
from src.routes.cities import router as cities_router
from src.routes.categories import router as categories_router
from src.routes.services import router as services_router

app = FastAPI(
    title="UrbanServe API",
    description="API para gestão de serviços e cidades integrada ao Supabase",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API rodando"}

app.include_router(users_router,tags=["users"])
app.include_router(cities_router,tags=["cities"])
app.include_router(categories_router,tags=["categories"])
app.include_router(services_router,tags=["services"])
