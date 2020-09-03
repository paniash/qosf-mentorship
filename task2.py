## Task 2 of the QOSF Mentooship programme
## To implement a circuit which returns |01> and |10> with equal probability

# Note the difference in the ordering of qubits in Qiskit

# Importing necessary libraries
from qiskit import *
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Define a quantum circuit of 2 qubits and 2 classical bits
qc = QuantumCircuit(2)
#qc.x(0)
qc.rx(np.pi, 0)

#qc.h(1)
qc.rx(np.pi/2, 1)
qc.rz(np.pi/2, 1)

qc.cx(1,0)
qc.measure_all()

backend = Aer.get_backend('qasm_simulator')

counts = execute(qc, backend).result().get_counts()
plot_histogram(counts)
#qc.draw()
plt.show()
