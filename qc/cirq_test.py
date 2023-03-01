import cirq

q1 = cirq.LineQubit(0)
q2 = cirq.LineQubit(1)

circuit = cirq.Circuit(
    cirq.X(q1),
    cirq.H(q2),
    cirq.SWAP(q1,q2),
    cirq.measure(q1, key='m'),
)

print(circuit)

sim = cirq.Simulator()

result = sim.run(circuit, repetitions=10)

print(result)