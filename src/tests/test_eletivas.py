from src.components.materias_component import (
    verificar_materias_disponiveis,
    adicionar_materia,
    get_materias
)

def main():

    materias_cursadas = set()
    get_materias()

    print("\nMatérias já cursadas:", materias_cursadas)

    tipo = input("\nMostrar (todas / obrigatorias / eletivas): ").lower()

    while True:

     
        materias_disponiveis = verificar_materias_disponiveis(
            materias_cursadas,
            tipo
        )

        print("\nMatérias disponíveis:")

        for m in materias_disponiveis:
            print(f"{m.codigo} - {m.nome}")

        codigo = input(
            "\nDigite o código de uma matéria cursada (ou 'sair', ou 'reiniciar'): "
        ).upper()

        if codigo == "SAIR":
            break

        if codigo == "REINICIAR":
            materias_cursadas.clear()
            continue

        if codigo not in get_materias():
            print("Matéria inválida.")
            continue

        materias_cursadas = adicionar_materia(
            materias_cursadas,
            codigo
        )

        print("DEBUG -> matérias cursadas:", materias_cursadas)


if __name__ == "__main__":
    main()