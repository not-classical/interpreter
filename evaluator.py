import tokenize
from parser import Parser
from product_system import ProductSystem


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
            text = input("(quil)> ")
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
            else:
                system.singleGate(parsed_object.name, parsed_object.qubit.number)

    print("\n Result: \n ")
    res = ""
    for i in system.collapse():
        res += str(i)

    print(f"|{res}>            100%")


if __name__ == "__main__":
    main()


# ans = tokenize.LexicalAnalyzer("CNOT 0 1 # I am a comment! ")
# ans2 = ans.lex()
# parser = Parser(ans2)