## Task 2 of the QOSF Mentooship programme
## To implement a circuit which returns |01> and |10> with equal probability

# Note the difference in the ordering of qubits in Qiskit

# Importing necessary libraries
from qiskit import *
import numpy as np
import matplotlib.pyplot as plt

# Define a quantum circuit of 2 qubits and 2 classical bits
qc = QuantumCircuit(2,2)
