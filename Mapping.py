from qiskit import QuantumCircuit
import matplotlib.pyplot as plt 

qc= QuantumCircuit(4)

a=0
b=0

if a :
    qc.x(0)
if b:
    qc.x(1)


qc.cx(0, 2)
qc.cx(1, 2)

# AND (carry) into qubit 3
qc.ccx(0, 1, 3)  # a AND b

# measure
qc.measure_all()


fig= qc.draw("mpl")
fig.savefig('and_circuit.png')
plt.show()
