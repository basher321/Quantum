from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

qc = QuantumCircuit(3)
qc.ccx(0,1,2)
fig= qc.decompose().draw('mpl')
fig.savefig('tswap_circuit.png')
plt.show()


