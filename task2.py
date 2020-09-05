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
import random

''' Circuit solution (trivial)
# Define a quantum circuit of 2 qubits
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
'''

# Define a quantum circuit of 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply an X gate on q_1 and a Hadamard gate on q_0
# Perform a CNOT with q_0 and q_1 being the control and target qubits respectively

# Randomize the parameters of
theta1 = random.uniform(0, 2*np.pi)
theta2 = random.uniform(0, 2*np.pi)
theta3 = random.uniform(0, 2*np.pi)
theta4 = random.uniform(0, 2*np.pi)

# RX gate on q_1 (to be optimized to X gate)
qc.rx(theta1, 1)

# Gates on q_0 (to be optimized to a Hadamard gate)
qc.ry(theta2, 0)
qc.rx(theta3, 0)
qc.ry(theta4, 0)

# CNOT gate
qc.cx(0,1)

# Measurement onto classical bits
qc.measure([0,1], [0,1])

# Backend = QASM simulator
backend = Aer.get_backend('qasm_simulator')

# Number of measurements
n = 1000

# Plot the measurement results on a histogram
counts = execute(qc, backend, shots = n).result().get_counts()
plot_histogram(counts)
plt.show()
