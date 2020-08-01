"""
Parser module - parses array of tokens and returns an AST or error
"""
from typing import List, Optional
from tokenize import Token
from qubit import Qubit
from program import *
from gates import *


class Parser:
    """
    Will parse different tokens and return an AST
    """

    def __init__(self, tokens: List[Token]):
        self.tokens: List[Token] = tokens
        self.current_token: Token
        self.pos: int = 0

    def eat(self) -> None:
        """
        Moves the token cursor forward and sets the new `current_token`
        """
        self.current_token = self.tokens[self.pos]
        self.pos += 1

    def peek(self) -> Token:
        """
        Returns the next token
        """
        return self.tokens[self.pos]

    def parse(self):
        """
        Parses tokens off to individual parse functions
        """
        elements = []
        while self.pos < len(self.tokens):
            curr_type = self.peek().token_type
            if curr_type is None:
                self.parse_none()
            elif curr_type == Token.GATE:
                elements.append(self.parse_gate())
            elif curr_type == Token.INSTRUCTION:
                elements.append(self.parse_instruction())
            elif curr_type == Token.VARIABLE:
                elements.append(self.parse_variable())
            elif curr_type == Token.TYPE:
                # Currently only implement int
                self.pos += 1

        return elements

    def parse_none(self) -> None:
        self.eat()
        if self.current_token.token_type is not None:
            raise TypeError(f"Unexpected token {self.current_token.value}")

    def parse_qubit(self) -> Qubit:
        """
        Parses a qubit
        """
        self.eat()
        if self.current_token.token_type is not Token.DIGIT:
            raise TypeError(f"Unexpected token {self.current_token.value}")

        qubit: Qubit = Qubit(int(self.current_token.value))
        return qubit

    def parse_gate(self) -> QuantumGate:
        """
        Parses a gate
        """
        self.eat()
        cnot, hadamard, identity, measure, paulix, pauliy, pauliz = [
            "CNOT",
            "H",
            "I",
            "MEASURE",
            "X",
            "Y",
            "Z",
        ]
        token: Token = self.current_token

        if self.current_token.token_type is not Token.GATE:
            raise TypeError(f"Unexpected token {token.value}")

        if token.value == cnot:
            self.parse_none()
            qubit1: Qubit = self.parse_qubit()
            self.parse_none()
            qubit2: Qubit = self.parse_qubit()
            return CNOT(qubit1, qubit2)

        else:
            self.parse_none()
            qubit: Qubit = self.parse_qubit()

            if token.value == identity:
                return Identity(qubit)
            elif token.value == paulix:
                return PauliX(qubit)
            elif token.value == pauliz:
                return PauliZ(qubit)
            elif token.value == pauliy:
                return PauliY(qubit)
            elif token.value == hadamard:
                return Hadamard(qubit)
            elif token.value == measure:
                self.parse_none()
                var: Variable = self.parse_variable()
                return Measure(qubit, var)

        raise TypeError("Unsupported gate")

    def parse_instruction(self):
        """
        Parses an instruction
        """
        self.eat()
        token: Token = self.current_token

        if token.token_type is not Token.INSTRUCTION:
            raise TypeError(f"Unexpected token {token.value}")

        self.parse_none()

        if token.value == "DECLARE":
            return self.parse_declare()
        elif token.value == "LABEL":
            return self.parse_label()
        elif token.value == "JUMP-WHEN":
            return self.parse_jump(1)
        elif token.value == "JUMP-UNLESS":
            return self.parse_jump(0)

        raise TypeError("Unsupported instruction")

    def parse_declare(self) -> Variable:
        """
        Parses a variable declaration

        Currently only implements variables of type int
        """
        var: Variable = self.parse_variable()

        t = self.parse_type()
        index = self.parse_index()
        var.index = index

        return var

    def parse_variable(self) -> Variable:
        """
        Parses a variable
        """
        self.eat()
        token: Token = self.current_token

        if token.token_type is not Token.VARIABLE:
            raise TypeError(f"Unexpected token {token.value}")

        name: str = token.value
        size: Optional[int] = self.parse_index()

        return Variable(name, size)

    def parse_index(self) -> Optional[int]:
        """
        Parses the size/index of a variable
        """
        if self.pos >= len(self.tokens):
            return None

        self.eat()
        token: Token = self.current_token

        if token.token_type is Token.INDEX:
            return int(token.value[1 : len(token.value) - 1])
        elif token.token_type is None:
            return None

        raise TypeError(f"Unexpected token {token.value}, {token.token_type}")

    def parse_type(self):
        """
        Parses the type
        """
        self.eat()
        token: Token = self.current_token

        if token.token_type is not Token.TYPE:
            raise TypeError(f"Unexpected token {token.value}")

        # Not yet implemented, currently only allows int
        return None

    def parse_label(self) -> Label:
        """
        Parses a label
        """
        self.eat()
        token: Token = self.current_token

        if token.token_type is not Token.LABEL:
            raise TypeError(f"Unexpected token {token.value}")

        return Label(token.value)

    def parse_jump(self, condition: int) -> Jump:
        """
        Parses a jump statement
        """
        label: Label = self.parse_label()
        self.parse_none()
        var: Variable = self.parse_variable()

        return Jump(label, var, condition)


import tokenize

ans = tokenize.LexicalAnalyzer("CNOT 0 1 # I am a comment! ")
ans2 = ans.lex()
parser = Parser(ans2)
