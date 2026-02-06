from qiskit import QuantumCircuit

def create_bell_state():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc
