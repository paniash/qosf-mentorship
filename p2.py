import pennylane as qml
from pennylane import numpy as np

dev0 = qml.device("default.qubit", wires=1)
dev1 = qml.device("default.qubit", wires=1)

@qml.qnode(dev0)
def qubit0(q0):
    qml.RY(q0[0], wires=0)
    qml.RX(q0[1], wires=0)
    return qml.probs(wires=0)

@qml.qnode(dev1)
def qubit1(q1):
    qml.RY(q1[0], wires=0)
    qml.RX(q1[1], wires=0)
    return qml.probs(wires=0)

#print(circuit([0,0], [0,0])[1,0])

def prob(circuit, params, state):
    return circuit(params)[state]

def cost0(x):
    return ((prob(qubit0, x, 0) - 0.5)**2 + (prob(qubit1, x, 1) - 0.5)**2)/4

def cost1(x):
    return (prob(qubit1, x, 0)**2 + (prob(qubit1, x, 1) - 1)**2)/4

init_params0 = [0.011, 0.012]
init_params1 = [0.011, 0.012]

opt = qml.GradientDescentOptimizer(stepsize=0.4)

steps = 100
params0 = init_params0
params1 = init_params1

for i in range(steps):
    params0 = opt.step(cost0, params0)

    if (i + 1) % 5 == 0:
        print("Cost after step {:5d}: {: .7f}".format(i + 1, cost0(params0)))

for j in range(steps):
    params1 = opt.step(cost1, params1)

    if (j + 1) % 5 == 0:
        print("Cost after step {:5d}: {: .7f}".format(j + 1, cost1(params1)))

# print("Optimized rotation angles for qubit 0: {}".format(params0))
# print("Optimized rotation angles for qubit 1: {}".format(params1))
print("Probability of qubit 0: {}".format(qubit0(params0)))
print("Probability of qubit 1: {}".format(qubit1(params1)))
