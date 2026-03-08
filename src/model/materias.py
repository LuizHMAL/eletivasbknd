from enum import Enum



class Materia:
    def __init__(self, nome: str, codigo: str, prerequisitos: list[str], obrigatoria: bool):
        self.nome = nome
        self.codigo = codigo
        self.prerequisitos = prerequisitos
        self.obrigatoria = obrigatoria

    def __repr__(self):
        return f"{self.codigo} - {self.nome}"


class TipoMateria(Enum):
    TODAS = "todas"
    OBRIGATORIAS = "obrigatorias"
    ELETIVAS = "eletivas"