from fastapi import FastAPI
from src.routes.users import router as users_router
from src.routes.cities import router as cities_router
from src.routes.categories import router as categories_router

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "API rodando"}

app.include_router(users_router)
app.include_router(cities_router)
app.include_router(categories_router)
