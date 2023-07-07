# Creating a parser to parse QASM code to QUA

## Abstract:
The goal of this project was to take the QASM code provided as an attribute in a JSON file, by the front end, and convert it to QUA code, Qua was the language that the OPX can understand and interpret, this language basically operates at pulse level and generates the individual pulses. This conversion was done with inspiration from how assembly code in classical computers is converted to machine language.  

## Procedure:
This process has 3 main steps.
 1. Fetching the JSON data and extracting the QASM code
 2. Converting the QASM to QUA code and adding the appropriate headers to make it run smoothly in the next step
 3. Inserting the generated script in a standard Python wrapper that can then be run.

We will look at all the 3 steps in detail.

### Step 1: the file parser
The JSON data is fetched from the TCS servers and is fed to our converter `convert.py` which uses the function from the builtin `JSON` library, `JSON.parse()` this line parses the value of a provided attribute line by line, stores it in the list `file_lines` and returns it.

### Step 2: the program
This is the main conversion step. It contains 2 main categories of functions, 

 1. The `line parser`
 2. The `keyword converters`

The `line_parse()` takes the individual lines returned by the `file parser` and reads the first member of the list `file_lines`, now according to WASM syntax, this will always be a keyword, we take this keyword and pass it through an if-elseif-else block that checks what this first value was and based on that send it to an appropriate function in the `keyword converters` block of functions.

The second block of functions basically has a list of functions that are named according to the keywords in QASM for example the hadamard gate is applied on a qubit using the keyword `h` so when the `line_parser()` read this as the first member of the `file_lines` list, it send the rest of the list to the function `h`.
Once function `h` gets control it reads the next menber of the list, which according to QASM systex will always be `;q[n]` where n is the qubit number to which gate `h` must be applied. so the function extracts this number n using `regex`. 
These 'keyword' functions take this number and output the corresponding lines of code for a `Hadamard` gate that would use a prebuilt macro that contains the set of `play()` commands. This putput is then written to a file QUA.py

The QUA.py file that is outputtedd is outputted with the headers:
```
from qm-qua import *
class MyClass:
    def QUA:
         with program() as output:
```
These headers allow this file to be standalone python file which we can instantiate in any other file, namely the `wrapper.py`

## Example:

QASM_code.txt:
```
qreg q[2]               #Initialize 2 Quantum Registers
creg c[2]               #Initialize 2 Classical registers, streams
h q[1]                  #apply hadamard gate to qubit 1
cx q[1] -> q[2]         #apply CNOT gate to qubit 2 with qubit 1 as control
measure q[2] -> c[2]    #measure qubit 2 on classical register/stream 2.

```
