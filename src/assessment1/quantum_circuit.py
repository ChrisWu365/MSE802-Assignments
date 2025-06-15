from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to qubit 0 (creates superposition)
qc.h(0)

# Apply CNOT gate (entangles qubits)
qc.cx(0, 1)

# Draw the circuit
fig = qc.draw(output='mpl')
plt.show()