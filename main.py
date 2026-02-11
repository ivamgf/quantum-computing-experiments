import sys

from config.settings import IBM_TOKEN, IBM_INSTANCE
from experiments.run_bell import run as run_bell
from experiments.run_teleportation import run as run_teleportation
from experiments.run_hypercube import run as run_hypercube


def validate_environment():
    if not IBM_TOKEN:
        raise EnvironmentError("IBM_QUANTUM_TOKEN não encontrado no .env")

    if not IBM_INSTANCE:
        raise EnvironmentError("IBM_QUANTUM_INSTANCE não encontrado no .env")


def print_usage():
    print("Uso:")
    print("  python main.py bell")
    print("  python main.py teleportation")
    print("  python main.py hypercube [dimensão] [caminho]")
    print("")
    print("Exemplo:")
    print("  python main.py hypercube 4 0 1 3 7")


def main():

    print("Inicializando aplicação quântica...")

    validate_environment()
    print("Credenciais carregadas com sucesso.")

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    experiment = sys.argv[1]
    print(f"Executando experimento: {experiment}")

    if experiment == "bell":
        run_bell()

    elif experiment == "teleportation":
        run_teleportation()

    elif experiment == "hypercube":

        if len(sys.argv) < 4:
            print("Erro: informe dimensão e caminho.")
            print_usage()
            sys.exit(1)

        try:
            dimension = int(sys.argv[2])
            path = list(map(int, sys.argv[3:]))

            # ✅ CORREÇÃO MATEMÁTICA
            max_vertex = 2 ** dimension

            if any(q >= max_vertex or q < 0 for q in path):
                raise ValueError(
                    f"Caminho inválido. Para dimensão {dimension}, "
                    f"use valores entre 0 e {max_vertex - 1}."
                )

        except ValueError as e:
            print("Erro nos parâmetros:", e)
            sys.exit(1)

        run_hypercube(dimension, path)

    else:
        print("Experimento não reconhecido.")
        print_usage()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Erro durante execução:", e)
        sys.exit(1)
