from qiskit_ibm_runtime import QiskitRuntimeService
from config.settings import (
    IBM_CHANNEL,
    IBM_TOKEN,
    IBM_INSTANCE,
    DEFAULT_BACKEND
)


# ==========================================
# 🔌 Inicializa serviço IBM
# ==========================================
def get_service():
    return QiskitRuntimeService(
        channel=IBM_CHANNEL,
        token=IBM_TOKEN,
        instance=IBM_INSTANCE
    )


# ==========================================
# 🖥 Seleciona backend
# ==========================================

def get_backend(simulator=False):
    service = get_service()
    if simulator:
        return service.get_backend("ibmq_qasm_simulator")
    return service.least_busy(simulator=False)
