import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer import AerSimulator

def solve_qaoa(qubo):
    n = len(qubo)

    # Create simple quantum circuit
    qc = QuantumCircuit(n, n)

    # Put all qubits in superposition
    for i in range(n):
        qc.h(i)

    # Measure all qubits
    qc.measure(range(n), range(n))

    # Run on simulator
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1024).result()

    counts = result.get_counts()

    # Get most frequent bitstring
    best = max(counts, key=counts.get)

   # Convert bitstring to ensure at least one stock selected
    solution = np.array([int(bit) for bit in best[::-1]])

   # Fix: ensure at least one 1 exists
    if np.sum(solution) == 0:
        solution[0] = 1

    return solution

