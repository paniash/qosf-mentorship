'''
Task 2 of the QOSF Mentorship programme
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
qc.ry(np.pi/2, 0)
qc.rx(np.pi, 0)

qc.cx(0,1)
qc.measure_all()

backend = Aer.get_backend('qasm_simulator')

# Number of measurements
n = 1000

counts = execute(qc, backend, shots = n).result().get_counts()
plot_histogram(counts)
plt.show()
'''

# Define a parametric quantum circuit of 2 qubits
def circuit(params):
    qc = QuantumCircuit(2)

    # Gates implemented
    qc.ry(params[0], 1)
    qc.rx(params[1], 1)
    qc.ry(params[2], 0)
    qc.rx(params[3], 0)

    return qc

# define backends
q_simulator = Aer.get_backend('qasm_simulator')
st_simulator = Aer.get_backend('statevector_simulator')

def prob(circuit, params, state, qubit)
