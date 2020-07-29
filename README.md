# The not so glorious !classical quil interpreter!
A Quil interpreter written in python :snake:

## Usage
Simply run the `interpreter.py` file, and the console will expect input from stdin.

```bash
python interpreter.py
```
Use `Ctrl-D` to stop interpreting.

You may use the following gates:
 * `H` 
 * `X` 
 * `Y` 
 * `Z` 
 * `I` 
 * `CNOT` 

Additionally we have provided some test for testing, in the quil_tests folder. Run the scripts like so
```bash
cat quil_tests/superdense_coding.quil | python evaluator.py
```
