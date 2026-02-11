import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# Credenciais IBM
# ===============================

IBM_CHANNEL = "ibm_cloud"
IBM_TOKEN = os.getenv("IBM_QUANTUM_TOKEN")
IBM_INSTANCE = os.getenv("IBM_QUANTUM_INSTANCE")

# ===============================
# ⚙ Configurações de Execução
# ===============================

DEFAULT_BACKEND = os.getenv("IBM_BACKEND")  # opcional no .env
SHOTS = int(os.getenv("IBM_SHOTS", 1024))

# ===============================
# Resultados
# ===============================

RESULTS_PATH = os.getenv("RESULTS_PATH", "results/")