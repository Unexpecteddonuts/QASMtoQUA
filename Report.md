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

The second block of functions basically has a list of functions that are named according to the keywords in QASM for example the hadamard gate is applied on a qubit using the keyword `h()` so when the `line_parser()` read this as the first member of the `file_lines` list, it send the rest of the list to the function `h()`.
Once function `h()` gets control it reads the next menber of the list, which according to QASM systex will always be `;q[n]` where n is the qubit number to which gate `h` must be applied. so the function extracts this number n using `regex`. 
These 'keyword' functions take this number and output the corresponding lines of code for a `Hadamard` gate that would use a prebuilt macro that contains the set of `play()` commands. This putput is then written to a file QUA.py

The QUA.py file that is outputtedd is outputted with the headers and footers:
```
from qm-qua import *
class MyClass:
    def QUA:
         # start QUA
         with program() as output:
     
         # end QUA
      return output
```
These headers and footers allow this file to be standalone python file which we can instantiate in any other file, namely the `wrapper.py`

## Example:

QASM_code.txt:
```
qreg q[2];               #Initialize 2 Quantum Registers
creg c[2];               #Initialize 2 Classical registers, streams
h q[1];                  #apply hadamard gate to qubit 1
cx q[1] -> q[2];,         #apply CNOT gate to qubit 2 with qubit 1 as control
measure q[2] -> c[2];    #measure qubit 2 on classical register/stream 2.

```

We will use this example to understand the codeflow of `converter.py`

- First the function `file_parse()` extracts the first line from the file, `qreg q[2]` and puts it in a list `file_lines` and returns it so now the contents of `file_lines` are `file_lines = ["qreg", "q[2];"]` 

- Then the function `line_parse()` takes `file_lines` and reads the first menber of the list, then it takes `file_lines[0]` and reads it and stores it in a string `match`, in this case its `qreg`. then through a conditional block it sends the command to the function whose name is stored in `match`. in this case its `qreg`

- The function `qreg(args)` yakes the list `file_lines` and reads `file_lines[1]`, which in this case is `"q[2];"`, and then using `regex` its able to exptract the number 2 and onve it does this it generates the required lines of initialisation which include `I` and `Q`.

Once this is complete, the program goes back to reading the second line and does the same process for the rest of the code. 

- for 2 qubit gates like CNOT and `measure` statements that have to qubits as arguments, the functions use regex to extract both the numbers. for example `CNOT_macro()` queries the 2nd and 4th members of the list `file_lines = ["cx", "q[1]", "->", "q[2];"]` and using regex extracts the qubut number on which the gate must be applied.

This is how it processes the `barrier`, `cx` and  `measure` keywords.

This goes on for all the lines in the file, the `EOF` trigger is used to send control to the `stream_processing()` function which adds th3 required lines of stream processing and the required footer `return output`.

## Specifications:
```
file_parse(filename)                    # takes filename as cli argument and reads lines sequentially 
line_parse(file_lines)                  # parses each line passed by file_parse() and puts into list
qreg(args)                              # initialisation of qubits guven in args
creg(args)                              # creates classical streams
h(args)                                 # Hadamard gate on qubit given in args
cx(args)                                # CNOT gate on qubits given in args
x(args)                                 # 180° phase rotation on x axis
sx(args)                                # 90° phase rotation on x axis (equiv of our Xby2 macro
sxdg(args)                              # -90° phase rotation on x axis (equiv of our mXby2 macro
y(args)                                 # 180° phase rotation on y axis
z(args)                                 # 180° phase rotation on z axis
barrier(args)                           # aligns qubit n to readout resonator n-1
measure(args, file_lines, save_lines)   # adds the measure and align statements and appends the save statements to list save_lines.
stream_processing(save_lines)           # adds the stream processing li es and the save lines
```

## Usage:
```
python3 convert.py [input_filename.JSON] > [output_file.py]
```
input_filename -> input file containing the JSON data with attribute QUA. [must be .JSON  or .txt filetype]

output_file.py -> file to pipeline the generated code.[must be .py filetype]
```
python3 wrapper.py
```