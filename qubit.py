"""
The Qubit class
"""


class Qubit:
    """
    Stored as a complex number
    """

    def __init__(self, number: int):
        """
        This is an int for now
        The number is the ID not the state
        """
        self.number = number

    def __repr__(self):
        return f"<Qubit with id {self.number}>"
