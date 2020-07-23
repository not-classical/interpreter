from qubit import Qubit


class QuantumGate:
    pass


class Hadamard(QuantumGate):
    def __init__(self, qubit: Qubit):
        self.qubit = qubit
        pass

    def __repr__(self):
        return f"<Hadamard with {self.qubit}>"


class CNOT(QuantumGate):
    def __init__(self, qubit1: Qubit, qubit2: Qubit):
        self.qubit1 = qubit1
        self.qubit2 = qubit2

    def __repr__(self):
        return f"<CNOT with {self.qubit1} and {self.qubit2}>"
