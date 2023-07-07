# Creating a parser to parse QASM code to QUA

## Abstract:
The goal of this project was to take the QASM code provided as an attribute in a JSON file, by the front end, and convert it to QUA code, Qua was the language that the OPX can understand and interpret, this language basically operates at pulse level and generates the individual pulses. This conversion was done with inspiration from how assembly code in classical computers is converted to machine language.  

## Procedure
This process has 3 main steps.
 - 1. Fetching the JSON data and extracting the QASM code
 - 2. Converting the QASM to QUA code and adding the appropriate headers to make it run smoothly in the next step
 - 3. Inserting the generated script in a standard python wrapper that can then be run.

We will look at all the 3 steps in detail.

### Step 1:
 - The JSON data is fetched from the TCS servers and is fed to our converter 'convert.py' which uses the function from the builtin 'JSON' library, 'JSON.parse()' this line parses the value of a provided attribute line by line and returns it.

## Step 2: the program
 - This is the main conversion step. It containes nain categories of functions, 

 - 1. The 'line parser'
 - 2. The 'keyword' converters

