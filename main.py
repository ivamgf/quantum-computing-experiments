import sys

from config.settings import IBM_TOKEN, IBM_INSTANCE
from experiments.run_bell import run as run_bell
from experiments.run_teleportation import run as run_teleportation


def validate_environment():
    """
    Verifica se as variáveis essenciais foram carregadas.
    """
    if not IBM_TOKEN:
        raise EnvironmentError("IBM_QUANTUM_TOKEN não encontrado no .env")

    if not IBM_INSTANCE:
        raise EnvironmentError("IBM_QUANTUM_INSTANCE não encontrado no .env")


def main():
    print("Inicializando aplicação quântica...")

    # 1️⃣ Validar ambiente
    validate_environment()
    print("Credenciais carregadas com sucesso.")

    # 2️⃣ Escolher experimento
    if len(sys.argv) < 2:
        print("Uso: python main.py [bell | teleportation]")
        sys.exit(1)

    experiment = sys.argv[1]
    print(f"Executando experimento: {experiment}")

    if experiment == "bell":
        run_bell()
    elif experiment == "teleportation":
        run_teleportation()
    else:
        print("Experimento não reconhecido.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Erro durante execução:", e)
        sys.exit(1)
