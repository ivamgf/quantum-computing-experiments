from qiskit import QuantumCircuit

def create_teleportation():
    qc = QuantumCircuit(3, 3)

    # Estado a ser teleportado
    qc.h(0)

    # Criar par de Bell
    qc.h(1)
    qc.cx(1, 2)

    # Operações de Bell measurement
    qc.cx(0, 1)
    qc.h(0)

    qc.measure([0, 1], [0, 1])
    qc.cx(1, 2)
    qc.cz(0, 2)

    qc.measure(2, 2)

    return qc
