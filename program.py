from typing import Optional, List


class Label:
    """
    Label represents a label for an instruction that
    can be jumped to during exectuion
    """

    def __init__(self, name: str):
        self.name = name


class Variable:
    """
    Variable represents either a raw value
    or a variable stored in memory
    """

    def __init__(self, name: str, index: Optional[int]):
        self.name = name
        self.index = index


class Jump:
    """
    Jump represents a an instruction to jump to
    """

    def __init__(self, label: Label, var: Variable, condition: int):
        self.label = label
        self.var = var
        self.condition = condition


class Program:
    """
    This class represents the exuction of the program
    """

    def __init__(self):
        self.program_counter = 0
        self.instructions = []
        self.variables = {}
        self.labels = {}

    def begin(self):
        self.program_counter = 0

    def instruction(self) -> str:
        """
        Return the current instruction and increment program counter
        """
        instruction = self.instructions[self.program_counter]
        self.program_counter += 1
        return instruction

    def add_instruction(self, instruction: str) -> None:
        """
        Add an instruction to the list of instructions
        """
        self.instructions.append(instruction)
        self.program_counter += 1

    def define_variable(self, var: Variable) -> None:
        """
        Define a variable in classical memory
        """
        if var.name in self.variables:
            raise ValueError(f"Variable already exists {var.name}")
        if var.index is None:
            self.variables[var.name] = 0
        else:
            self.variables[var.name] = [0] * var.index

    def set_variable(self, var: Variable, val) -> None:
        """
        Set the value of a variable in classical memory
        """
        if var.name not in self.variables:
            raise ValueError(f"Variable does not exist {var.name}")
        if var.index == None:
            self.variables[var.name] = val
        else:
            self.variables[var.name][var.index] = val

    def get_val(self, var: Variable):
        """
        Get the value of a variable in classical memory
        """
        if not var.name in self.variables:
            raise ValueError(f"Variable does not exist {var.name}")
        if var.index == None:
            return self.variables[var.name]
        return self.variables[var.name][var.index]

    def set_label(self, label: Label) -> None:
        """
        Add a label and corresponding instruction index to label dictionary
        """
        if label.name in self.labels:
            raise ValueError(f"Label already exists {label.name}")
        self.labels[label.name] = self.program_counter - 1

    def jump(self, jump: Jump) -> None:
        """
        Jump to an instruction in a different part of the program
        """
        if jump.label.name not in self.labels:
            raise ValueError(f"Unexpected label {jump.label.name}")
        var: int = self.get_val(jump.var)
        if var == jump.condition:
            self.program_counter = self.labels[jump.label.name]

    def is_complete(self) -> bool:
        """
        Program is complete if program counter is beyond end of instruction list
        """
        return self.program_counter >= len(self.instructions)

    def print_memory(self) -> None:
        """
        Prints the contents in classical memory
        """
        print("Classical memory:")
        for var_name in self.variables:
            var = self.variables[var_name]
            if isinstance(var, List):
                print(f"  {var_name}: [", end="")
                for i in range(len(var) - 1):
                    print(f"{var[i]}, ", end="")
                print(f"{var[len(var) - 1]}]")
            else:
                print(f"  {var_name}: {var}")
        print()
