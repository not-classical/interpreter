import tokenize
from parser import Parser
from product_system import ProductSystem
from program import *


def print_proba(vector_prob: list):
    """
    Input is like [(01, 0.5555)]
    Print the probabities like this
    |00>    100%
    |01>      0%
    """
    for vec, prob in sorted(vector_prob):
        print(f"|{vec}>\tP = {round(prob * 100, 6)}%")


def main():
    print(
        """
     _      _               _           _
    | |    | |             (_)         | |
    | | ___| | __ _ ___ ___ _  ___ __ _| |
    | |/ __| |/ _` / __/ __| |/ __/ _` | |
    |_| (__| | (_| \__ \__ \ | (_| (_| | |
    (_)\___|_|\__,_|___/___/_|\___\__,_|_|

    Welcome to the glorious !classical quil interpreter!

    To exit, use Ctrl-D
    """
    )
    system = ProductSystem(2)
    program = Program()

    # Read all instructions and set labels
    while True:
        try:
            text = input()
            if not text:
                continue

            # Define position of labels
            tokens = tokenize.LexicalAnalyzer(text).lex()
            parsed_object = Parser(tokens).parse()

            program.add_instruction(text)
            if len(parsed_object) > 0 and isinstance(parsed_object[0], Label):
                program.set_label(parsed_object[0])

        except EOFError:
            break

    # Begin actual execution
    program.program_counter = 0
    while not program.is_complete():
        tokens = tokenize.LexicalAnalyzer(program.instruction()).lex()
        parsed_output = Parser(tokens).parse()
        for parsed_object in parsed_output:

            if isinstance(parsed_object, Label):
                break  # skip because labels are set on first pass
            elif isinstance(parsed_object, Variable):
                program.define_variable(parsed_object)
            elif isinstance(parsed_object, Jump):
                program.jump(parsed_object)
            elif parsed_object.name == "CNOT":
                system.multiGate(
                    "CNOT", parsed_object.qubit1.number, parsed_object.qubit2.number
                )
            elif parsed_object.name == "MEASURE":
                measurement = system.measure(parsed_object.qubit.number)
                program.set_variable(parsed_object.var, measurement)
            else:
                system.singleGate(parsed_object.name, parsed_object.qubit.number)

    print_proba(system.get_probabilities())

    print("\n Result after collapse: \n ")
    res = ""
    for i in system.collapse():
        res += str(i)

    print(f"|{res[::-1]}>\t100%")


if __name__ == "__main__":
    main()


# ans = tokenize.LexicalAnalyzer("CNOT 0 1 # I am a comment! ")
# ans2 = ans.lex()
# parser = Parser(ans2)
