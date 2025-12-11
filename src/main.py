from fastapi import FastAPI
from src.routes.users import router as users_router

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "API rodando"}

app.include_router(users_router)
