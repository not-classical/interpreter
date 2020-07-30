import tokenize
from parser import Parser
from product_system import ProductSystem


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
    while True:
        try:
            text = input()
        except EOFError:
            break
        if not text:
            continue
        tokens = tokenize.LexicalAnalyzer(text).lex()
        parsed_output = Parser(tokens).parse()
        for parsed_object in parsed_output:

            if parsed_object.name == "CNOT":
                system.multiGate(
                    "CNOT", parsed_object.qubit1.number, parsed_object.qubit2.number
                )
            elif parsed_object.name == "MEASURE":
                system.measure(parsed_object.qubit.number)
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
