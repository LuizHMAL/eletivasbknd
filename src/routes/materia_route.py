from fastapi import APIRouter, HTTPException
from src.components.materias_component import get_materias, get_materia
from src.model.materias import MateriasResponse, MateriaSimpleSelectResponse

router = APIRouter()

@router.get("/materias/{tipo}", response_model=MateriasResponse)
def listar_materias(tipo: str = "todas"):
    materias_dict = get_materias(tipo)

    if not materias_dict:
        raise HTTPException(status_code=404, detail="Tipo de matéria inválido.")

    return MateriasResponse(materias=list(materias_dict.values()))

@router.get("/materia/{codigo}", response_model = MateriaSimpleSelectResponse)
def obter_materia(codigo:str):
    materia = get_materia(codigo)

    if not materia:
        raise HTTPException(status_code=404, detail="Matéria não encontrada.")

    return MateriaSimpleSelectResponse(codigo=materia.codigo, nome=materia.nome)

