from src.components.materias_component import verificar_materias_disponiveis

def main():
    materias_cursadas = []

    while True:
        print("\nMatérias já cursadas:", materias_cursadas)

        tipo = input("\nMostrar (todas / obrigatorias / eletivas): ").lower()

        materias_disponiveis = verificar_materias_disponiveis(materias_cursadas, tipo)

        print("\nMatérias disponíveis:")
        for m in materias_disponiveis:
            print(f"{m.codigo} - {m.nome}")

        codigo = input("\nDigite o código de uma matéria cursada (ou 'sair, ou reiniciar'): ")

        if codigo.lower() == "sair":
            break

        if codigo.lower() == "reiniciar":
            materias_cursadas.clear()
            continue

        materias_cursadas.append(codigo)


if __name__ == "__main__":
    main()