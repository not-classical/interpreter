# An test repr
import numpy as np
import math

from typing import Union

class Token():
    def __init__(self, token_type: str, value: Union[str,int]):
        """
        For now just gates and qubits
        """
        self.token_type = token_type
        self.value = value

class Gate():
    pass

class Hadamard(Gate):
    def __init__(self):
        pass

class Qubit():
    def __init__(self, qubit_id:int, state: int = None):
        self.qubit_id = qubit_id
        self.state = state if state else 0

    def entangle_with(self, qubit: 'Qubit'):
        # entangle with another qubit?
        pass

    def update_state(self, gate):
        pass


class Interpreter():
    def __init__(self, text:str) -> Token:
        self.text = text
        self.position = 0
        self.current_token = None

    def get_next_token(self):
        text = self.text

        if self.position > len(text) - 1:
            return Token("EOF", None)

        current_char: str = text[self.position]
        token: Token = None

        if current_char == 'H':
            token = Token('GATE', current_char)
        elif current_char.isdigit():
            token = Token('QUBIT', current_char)

        self.position += 1
        return token

    def eat(self):
        self.current_token = self.get_next_token()

    def evaluate(self):
        """
        Expressions only of the form <GATE> <QUBIT>
        """
        self.eat()
        gate: Gate = None
        if (self.current_token.token_type == "GATE"):
            if (self.current_token.value == "H"):
                gate = Hadamard()

        self.eat()
        while(self.current_token is None):
            self.eat()

        qubit: Qubit = self.current_token

        if (self.current_token.token_type == "QUBIT"):
            qubit = Qubit(self.current_token.value)

        return (gate, qubit)

def main():
    print("""
     _      _               _           _
    | |    | |             (_)         | |
    | | ___| | __ _ ___ ___ _  ___ __ _| |
    | |/ __| |/ _` / __/ __| |/ __/ _` | |
    |_| (__| | (_| \__ \__ \ | (_| (_| | |
    (_)\___|_|\__,_|___/___/_|\___\__,_|_|

    Welcome to the glorious !classical quil interpreter!

    To exit, use Ctrl-D
    """)
    bits = []
    while True:
        try:
            text = input('(quil)> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        gate, qubit = interpreter.evaluate()
        bits.append((gate, qubit))

        print(f"You currently have {len(bits)} qubit(s) active: \n")
        for bit in bits:
            print(f"{bit[1].qubit_id} with gate {bit[0]}")

if __name__ == "__main__":
    main()

