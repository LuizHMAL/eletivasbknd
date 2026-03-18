from fastapi import FastAPI
from src.routes.materia_route import router as materias_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(materias_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Eletivas!"}