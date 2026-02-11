from qiskit import QuantumCircuit
import numpy as np


def create_hypercube_teleport_circuit(n, path):

    num_steps = len(path) - 1
    total_qubits = 3 * num_steps

    qc = QuantumCircuit(total_qubits, total_qubits)

    for step in range(num_steps):

        q_source = 3 * step
        q_epr    = 3 * step + 1
        q_target = 3 * step + 2

        # Estado arbitrário
        qc.ry(np.pi/4, q_source)
        qc.rz(np.pi/6, q_source)

        # Criar EPR
        qc.h(q_epr)
        qc.cx(q_epr, q_target)

        # Protocolo unitário equivalente (sem medição intermediária)
        qc.cx(q_source, q_epr)
        qc.h(q_source)

        qc.cx(q_epr, q_target)
        qc.cz(q_source, q_target)

        qc.barrier()

    qc.measure_all()

    return qc
