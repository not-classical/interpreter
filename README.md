# The not so glorious !classical quil interpreter!
A Quil interpreter written in python :snake:

## Usage
Simply run the `interpreter.py` file, and the console will expect input from stdin.

```bash
python interpreter.py
```
Use `Ctrl-D` to stop interpreting and output probablitites.

You may use the following quantum gates:
 * `H` 
 * `X` 
 * `Y` 
 * `Z` 
 * `I` 
 * `CNOT` 
 * `MEASURE` 

Additionally we have provided some test for testing, in the quil_tests folder. Run the scripts like so
```bash
cat quil_tests/superdense_coding.quil | python evaluator.py
```
