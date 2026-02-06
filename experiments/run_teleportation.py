import os
from datetime import datetime

from qiskit import transpile
from qiskit_ibm_runtime import Sampler

from infrastructure.ibm_service import get_backend
from circuits.teleportation import create_teleportation
from experiments.plot_utils import plot_counts

RESULTS_DIR = "results"


def save_results_txt(backend_name, counts, raw_result):
    """
    Salva os resultados do experimento de teletransporte em arquivo TXT.
    """
    os.makedirs(RESULTS_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(RESULTS_DIR, f"teleportation_result_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=== EXPERIMENTO: TELETRANSPORTE QUÂNTICO ===\n")
        f.write(f"Data/Hora: {timestamp}\n")
        f.write(f"Backend: {backend_name}\n")
        f.write(f"Shots: {sum(counts.values())}\n\n")

        f.write("Distribuição de Resultados:\n")
        for state, value in counts.items():
            f.write(f"{state}: {value}\n")

        f.write("\n=== RAW RESULT ===\n")
        f.write(str(raw_result))

    print(f"Resultados salvos em: {filename}")

def run():
    backend = get_backend(simulator=False)

    print(f"Backend selecionado: {backend.name}")

    qc = create_teleportation()

    # Transpilar para o backend físico
    transpiled_qc = transpile(qc, backend=backend)

    print("Enviando job de teletransporte...")

    sampler = Sampler(backend)
    job = sampler.run([transpiled_qc])

    result = job.result()

    pub_result = result[0]

    # Forma compatível com versões diferentes do runtime
    if hasattr(pub_result.data, "meas"):
        counts = pub_result.data.meas.get_counts()
    elif hasattr(pub_result.data, "c"):
        counts = pub_result.data.c.get_counts()
    else:
        counts = pub_result.data.get_counts()

    print("Resultados Teleportation:", counts)

    print(result)

    # Salvar TXT
    save_results_txt(backend.name, counts, result)

    plot_counts(
        counts,
        title="Distribuição Experimental - Teletransporte Quântico",
        filename="teleportation_result.png"
    )
