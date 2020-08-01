from qubit import Qubit
from program import Variable
import numpy as np
from cmath import sqrt
import random


class QuantumGate:
    pass


class Identity(QuantumGate):
    name = "I"

    def __init__(self, qubit: Qubit):
        self.qubit = qubit

    def __repr__(self):
        return f"<Identity with {self.qubit}>"


class Hadamard(QuantumGate):
    name = "H"

    def __init__(self, qubit: Qubit):
        self.qubit = qubit

    def __repr__(self):
        return f"<Hadamard with {self.qubit}>"


class Measure(QuantumGate):
    name = "MEASURE"

    def __init__(self, qubit: Qubit, var: Variable):
        self.qubit = qubit
        self.var = var

    def __repr__(self):
        return f"<MEASURE with qubit {self.qubit}>"


class PauliZ(QuantumGate):
    name = "Z"

    def __init__(self, qubit: Qubit):
        self.qubit = qubit

    def __repr__(self):
        return f"<Z with {self.qubit}>"


class PauliX(QuantumGate):
    name = "X"

    def __init__(self, qubit: Qubit):
        self.qubit = qubit

    def __repr__(self):
        return f"<X with {self.qubit}>"


class PauliY(QuantumGate):
    name = "Y"

    def __init__(self, qubit: Qubit):
        self.qubit = qubit

    def __repr__(self):
        return f"<Y with {self.qubit}>"


class CNOT(QuantumGate):
    name = "CNOT"

    def __init__(self, qubit1: Qubit, qubit2: Qubit):
        self.qubit1 = qubit1
        self.qubit2 = qubit2

    def __repr__(self):
        return f"<CNOT with {self.qubit1} and {self.qubit2}>"
