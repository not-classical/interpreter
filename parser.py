"""
Parser module - parses array of tokens and returns an AST or error
"""
from typing import List

from tokenize import Token
from qubit import Qubit
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

        raise TypeError("Unsupported gate")


import tokenize

ans = tokenize.LexicalAnalyzer("CNOT 0 1 # I am a comment! ")
ans2 = ans.lex()
parser = Parser(ans2)
