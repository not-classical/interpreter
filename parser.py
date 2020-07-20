"""
Parser module - parses array of tokens and returns an AST or error
"""
from typing import List

from tokenize import Token
from qubit import Qubit
from gates import QuantumGate, Hadamard


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
        Parses a gate. Currently we have:
         - Hadamard
        """
        self.eat()
        CNOT, HADAMARD, IDENTITY, MEASURE = ["CNOT", "H", "I", "MEASURE"]
        token: Token = self.current_token

        if self.current_token.token_type is not Token.GATE:
            raise TypeError(f"Unexpected token {token.value}")

        if token.value == HADAMARD:
            self.parse_none()
            qubit: Qubit = self.parse_qubit()
            return Hadamard(qubit)

        else:
            raise TypeError("Unsupported gate")


import tokenize

ans = tokenize.LexicalAnalyzer("H 0 # dfadsk;jf;ladksjf;lak j")
ans2 = ans.lex()
parser = Parser(ans2)
