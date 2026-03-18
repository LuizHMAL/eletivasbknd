from enum import Enum
from pydantic import BaseModel






class Materia(BaseModel):
    nome: str
    codigo: str
    prerequisitos: list[str]
    obrigatoria: bool

    def __repr__(self):
        return f"{self.codigo} - {self.nome}"


class TipoMateria(Enum):
    TODAS = "todas"
    OBRIGATORIAS = "obrigatorias"
    ELETIVAS = "eletivas"

class MateriasResponse(BaseModel):
    materias: list[Materia]


class MateriaSimpleSelectResponse(BaseModel):
    codigo: str
    
    