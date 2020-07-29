"""
These are all the possible type for the interpreter to interpret

We can add more as we go on
"""
import sys
import re

from typing import List, Optional, Pattern, Tuple, Union


class Token:
    """
    This is the token class, with the current types being
     - LETTER
     - DIGIT
     - SEMICOLON
     - SPACE
     - HASH (COMMENT)
    """

    LETTER, DIGIT, SEMICOLON, INSTRUCTION, GATE = [
        "LETTER",
        "DIGIT",
        "SEMI-COLON",
        "INSTRUCTION",
        "GATE",
    ]

    def __init__(self, token_type: Optional[str], value: Union[str, int]):
        """
        For now just gates and qubits
        """
        self.token_type = token_type
        self.value = value

    def __repr__(self) -> str:
        return f"<{self.token_type} :: {self.value}>"


class LexicalAnalyzer:
    """
    Lexes input to `Token` types
    """

    token_expressions: List[Tuple[str, Optional[str]]] = [
        (r"[ \n\t]+", None),  # Spaces
        (r"#[^\n]*", None),  # Regex for comments
        (r";", Token.SEMICOLON),
        (r"DEFGATE", Token.INSTRUCTION),
        (r"DEFCIRCUIT", Token.INSTRUCTION),
        (r"MEASURE", Token.GATE),
        (r"CNOT", Token.GATE),
        (r"NOP", Token.GATE),
        (r"X", Token.GATE),
        (r"H", Token.GATE),
        (r"I", Token.GATE),
        (r"Y", Token.GATE),
        (r"Z", Token.GATE),
        (r"[0-9]+", Token.DIGIT),
    ]

    def __init__(self, text: str):
        self.text = text

    def lex(self) -> List[Token]:
        """
        Returns an array of tokens

        Will exit with error if the tokens don't match
        """
        pos = 0
        out = []
        while pos < len(self.text):
            match = None
            for token_expression in self.token_expressions:
                pattern: str
                type_value: Optional[str]
                pattern, type_value = token_expression

                regex = re.compile(pattern)
                match = regex.match(self.text, pos)

                if match:
                    token_value: str = match.group(0)
                    if token_value:
                        token = Token(type_value, token_value)
                        out.append(token)
                    break
            if match is None:
                sys.stderr.write(f"Illegal sequence: {self.text[pos]}\n")
                sys.exit()
            else:
                pos = match.end(0)

        return out
