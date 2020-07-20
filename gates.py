from qubit import Qubit


class QuantumGate:
    pass


class Hadamard(QuantumGate):
    def __init__(self, qubit: Qubit):
        self.qubit = qubit
        pass

    def __repr__(self):
        return f"<Hadamard with {self.qubit}>"
