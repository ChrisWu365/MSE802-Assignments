from qiskit import QuantumCircuit
from qiskit.visualization import plot_circuit_layout
import matplotlib.pyplot as plt

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard to qubit 0
qc.h(0)

# Apply CNOT with control=0, target=1
qc.cx(0, 1)

# Draw the circuit
qc.draw('mpl')  # 'mpl' uses Matplotlib to render as image
plt.show()
