from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc= QuantumCircuit(1,1)
qc.measure(0,0)
fig= qc.draw('mpl')
fig.savefig('measure_circuit.png')
plt.show()

