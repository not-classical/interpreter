# The not so glorious !classical quil interpreter!
A Quil interpreter written in python :snake:

## Usage
Simply run the `interpreter.py` file, and the console will expect input from stdin.

```bash
python interpreter.py
```
Use `Ctrl-D` to stop interpreting and output probablitites.

Additionally we have provided some quil programs for testing, in the `quil_tests` folder. Run the scripts like so
```bash
cat quil_tests/superdense_coding.quil | python interpreter.py
```

## Supported instructions

You may use the following quantum gates:
 * `H` 
 * `X` 
 * `Y` 
 * `Z` 
 * `I` 
 * `CNOT` 
 * `MEASURE` 
 
You can declare classical memory with `DECLARE` and control the flow of operations with `LABEL`s and `JUMPS`

## (Currently) unsupported operations

`DEFGATE` and `DEFCIRCUIT`, as well as most operations on classical memory (`ADD`, `MOV`, `MUL`)
