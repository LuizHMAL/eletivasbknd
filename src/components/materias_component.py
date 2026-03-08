import json
from typing import Dict, List, Optional
from src.model.materias import Materia


with open("src/data/materias.json", encoding="utf-8") as f:
    data: dict = json.load(f)


materias: Dict[str, Materia] = {}


def get_materias() -> Dict[str, Materia]:
    if materias:
        return materias

    for codigo, m in data["disciplinas"].items():
        materias[codigo] = Materia(
            nome=m["nome"],
            codigo=codigo,
            prerequisitos=m["prerequisitos"],
            obrigatoria=m["obrigatoria"]
        )

    return materias


def get_materia(codigo: str) -> Optional[Materia]:
    return get_materias().get(codigo)


def verificar_prerequisitos(materias_cursadas: List[str], materia: Materia) -> bool:
    return all(pr in materias_cursadas for pr in materia.prerequisitos)

def verificar_materias_disponiveis(
    materias_cursadas: List[str],
    tipo: str = "todas"
) -> List[Materia]:

    materias_disponiveis: List[Materia] = []

    for materia in get_materias().values():

        if materia.codigo in materias_cursadas:
            continue

        if not verificar_prerequisitos(materias_cursadas, materia):
            continue

        if tipo == "eletivas" and materia.obrigatoria:
            continue

        if tipo == "obrigatorias" and not materia.obrigatoria:
            continue

        materias_disponiveis.append(materia)

    return materias_disponiveis



for codigo, materia in get_materias().items():
    print(codigo, materia.nome)



for codigo, materia in get_materias().items():
    if materia.obrigatoria:
        print(f"{codigo} - {materia.nome} é obrigatória")



for codigo, materia in get_materias().items():
    if not materia.obrigatoria:
        print(f"{codigo} - {materia.nome} é eletiva")