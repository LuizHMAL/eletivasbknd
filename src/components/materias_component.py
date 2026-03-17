import json
from typing import Dict, List, Optional, Set
from src.model.materias import Materia


with open("src/data/materias.json", encoding="utf-8") as f:
    data: dict = json.load(f)


materias: Dict[str, Materia] = {}
materias_cursadas: Set[str] = set()

cache = {}

def get_materias(tipo: str) -> Dict[str, Materia]:
    if tipo in cache:
        return cache[tipo]

    materias = {}

    for codigo, m in data["disciplinas"].items():
        if tipo == "todas":
            pass
        elif tipo == "obrigatorias" and not m["obrigatoria"]:
            continue
        elif tipo == "eletivas" and m["obrigatoria"]:
            continue

        materias[codigo] = Materia(
            nome=m["nome"],
            codigo=codigo,
            prerequisitos=m["prerequisitos"],
            obrigatoria=m["obrigatoria"]
        )

    cache[tipo] = materias
    return materias






    
def get_materia(codigo: str) -> Optional[Materia]:
    return get_materias().get(codigo)







def verificar_prerequisitos(materias_cursadas: Set[str], materia: Materia) -> bool:
    return all(pr in materias_cursadas for pr in materia.prerequisitos)


def verificar_materias_disponiveis(
    materias_cursadas: Set[str],
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
        print("DEBUG -> matéria disponível:", materia.codigo, "-", materia.nome)
        materias_disponiveis.append(materia)
        
    return materias_disponiveis


def adicionar_materia(
    materias_cursadas: Set[str],
    codigo: str
) -> Set[str]:

    if codigo in materias_cursadas:
        return materias_cursadas

    materia = get_materia(codigo)

    if not materia:
        return materias_cursadas

    materias_cursadas.add(codigo)

    for pr in materia.prerequisitos:
        adicionar_materia(materias_cursadas, pr)

    return materias_cursadas