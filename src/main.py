from fastapi import FastAPI
from src.routes.materia_route import router as materias_router

app = FastAPI()
app.include_router(materias_router)


@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Eletivas!"}