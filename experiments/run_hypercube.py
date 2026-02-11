from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import Sampler
from infrastructure.ibm_service import get_backend
from circuits.hypercube_teleport import create_hypercube_teleport_circuit
from config.settings import SHOTS, RESULTS_PATH
import datetime
import os

from visualization.hypercube_plot import plot_hypercube


def run(n, path):

    print(f"Executando hipercubo de dimensão {n}")
    print(f"Caminho: {path}")

    backend = get_backend()

    qc = create_hypercube_teleport_circuit(n, path)

    pass_manager = generate_preset_pass_manager(
        backend=backend,
        optimization_level=1
    )

    transpiled = pass_manager.run(qc)

    # ✅ Runtime atualizado
    sampler = Sampler(mode=backend)

    job = sampler.run([transpiled], shots=SHOTS)
    result = job.result()

    # Criar pasta se não existir
    os.makedirs(RESULTS_PATH, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(
        RESULTS_PATH,
        f"hypercube_{timestamp}.txt"
    )

    with open(file_path, "w") as f:
        f.write(str(result))

    print("Resultados salvos em:", file_path)

    print("Gerando visualização do hipercubo...")
    plot_hypercube(n, path)

    return result
