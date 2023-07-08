import re
def stream_count():
    file_path = "qasm_code.txt"                                                                                                                                                                                             
    with open(file_path, 'r') as file:                                                                                                                                                                                      
        lines = file.readlines()                                                                                                                                                                                            
        for line in lines:                                                                                                                                                                                                  
            if line.startswith("creg"):                                                                                                                                                                                     
                match = re.search(r'c\[(\d+)\]', line)                                                                                                                                             
                if match:                                                                                                                                                                                                   
                    qubits = int(match.group(1))
                    return(qubits)
