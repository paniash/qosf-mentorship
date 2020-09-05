'''
Task 2 of the QOSF Mentooship programme
To implement a circuit which returns |01> and |10> with equal probability
'''

# Note the difference in the ordering of qubits in Qiskit

# Importing necessary libraries
from qiskit import *
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Define a quantum circuit of 2 qubits and 2 classical bits
qc = QuantumCircuit(2)

# X gate
qc.rx(np.pi, 1)

# Hadamard gate
qc.ry(np.pi/4, 0)
qc.rx(np.pi, 0)
qc.ry(-np.pi/4, 0)

qc.cx(0,1)
qc.measure_all()

backend = Aer.get_backend('qasm_simulator')

# Number of measurements
n = 1000

counts = execute(qc, backend, shots = n).result().get_counts()
plot_histogram(counts)
plt.show()
