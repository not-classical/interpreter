import numpy as np
from cmath import sqrt
import random


class ProductSystem:
    gates = {
        "H": (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]]),
        "X": np.array([[0, 1], [1, 0]]),
        "Y": np.array([[0, -1j], [1j, 0]]),
        "Z": np.array([[1, 0], [0, -1]]),
        "I": np.array([[1, 0], [0, 1]]),
        "CNOT": np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]),
        "SWAP": np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]),
    }

    def __init__(self, qubits):
        self.state = np.transpose(np.array([1, 0]))  # |0>
        self.qubits = 1
        for i in range(qubits - 1):
            self.add()

    def add(self):
        self.state = np.kron(self.state, np.transpose(np.array([1, 0])))
        self.qubits += 1

    def singleGate(self, gate, target):
        if target > self.qubits - 1:
            for _ in range(target - self.qubits + 1):
                self.add()
        gateMatrix = np.array([1])
        for i in range(self.qubits):
            if i == target:
                gateMatrix = np.kron(gateMatrix, self.gates[gate])
            else:
                gateMatrix = np.kron(gateMatrix, self.gates["I"])

        self.state = np.matmul(gateMatrix, self.state)

    def multiGate(self, gate, control, target):

        if target > self.qubits - 1:
            for _ in range(target - self.qubits + 1):
                self.add()

        if control > self.qubits - 1:
            for _ in range(control - self.qubits + 1):
                self.add()

        swapMatrix = np.identity(2 ** self.qubits)
        reverseMatrix = np.identity(2 ** self.qubits)

        n = max(control, target)
        m = min(control, target)
        difference = abs(control - target)

        for i in range(difference):
            if target > control and i == difference - 1:
                break
            SWAP = self.constructGate("SWAP", n - 1)
            n = n - 1
            swapMatrix = np.matmul(SWAP, swapMatrix)
            reverseMatrix = np.matmul(reverseMatrix, SWAP)

        gateMatrix = self.constructGate(gate, m)

        self.state = np.matmul(swapMatrix, self.state)
        self.state = np.matmul(gateMatrix, self.state)
        self.state = np.matmul(reverseMatrix, self.state)

    def constructGate(self, gate, target):
        gateMatrix = np.array([1])
        for i in range(self.qubits - 1):
            if i == target:
                gateMatrix = np.kron(gateMatrix, self.gates[gate])
            else:
                gateMatrix = np.kron(gateMatrix, self.gates["I"])
        return gateMatrix

    def measure(self, target):
        probabilities = abs(self.state ** 2)
        outcomes = []
        m = max(probabilities)
        for i in range(2 ** self.qubits):
            if probabilities[i] == m:
                outcomes += [i]

        targetOutcomes = [[], []]
        value = 0
        for i in range(0, 2 ** self.qubits, 2 ** (self.qubits - (target + 1))):
            for outcome in outcomes:
                if outcome in range(i, i + (2 ** (self.qubits - (target + 1)))):
                    targetOutcomes[0] += [outcome] if value == 0 else []
                    targetOutcomes[1] += [outcome] if value == 1 else []
            value = 1 if value == 0 else 0

        if len(targetOutcomes[0]) == 0:
            return 1
        elif len(targetOutcomes[1]) == 0:
            return 0
        else:
            targetState = random.choice([0, 1])
            self.adjust(targetOutcomes[targetState])
            return targetState

    def adjust(self, outcomes):
        self.state = self.state.astype(complex)
        for i in range(2 ** self.qubits):
            if i in outcomes:
                self.state[i] = sqrt(self.state[i])
                if len(outcomes) == 1:
                    self.state[i] = 1
            else:
                self.state[i] = 0

    def _vector_comb(self, number: int, ans=None):
        """
        Return the combinations of the vectors for example:
        00 01 10 11
        """
        new_ans = []
        if number == 0:
            return ans
        if ans is None:
            new_ans.append("0")
            new_ans.append("1")
        else:
            for i in ans:
                new_ans.append(i + "0")
                new_ans.append(i + "1")

        return self._vector_comb(number - 1, new_ans)

    def get_probabilities(self):
        """
        Return probability vector
        """
        probabilities = abs(self.state ** 2)
        vectors = self._vector_comb(self.qubits)
        vectors = [elem[::-1] for elem in vectors]
        return list(zip(vectors, probabilities))

    def collapse(self):
        probabilities = abs(self.state ** 2)
        m = max(probabilities)
        outcomes = []
        for i in range(2 ** self.qubits):
            if probabilities[i] == m:
                outcomes += [i]

        index = random.choice(outcomes)
        self.state = self.state * 0
        self.state[index] = 1
        return self.result(index)

    def result(self, outcome):
        result = []
        for target in range(self.qubits):
            value = 0
            for i in range(0, 2 ** self.qubits, 2 ** (self.qubits - (target + 1))):
                if outcome in range(i, i + (2 ** (self.qubits - (target + 1)))):
                    result += [value]
                    break
                value = 1 if value == 0 else 0
        return result
