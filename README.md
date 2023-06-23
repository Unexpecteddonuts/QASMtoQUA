# QASMtoQUA
A python parser to parse OPENQASM 2.0 to QUA(Quantum Universal Assembly)

# TBD
1. The QASM data will be received a JSON with headers proc_id, rec_time, QASM_code, h_score, will use the `json.loads()` function from the `json` library
   - the proc_id data will be used to identify the data before and after preprocessing and then after the hardware processing.
   - the rec_time data will be used to store the the submition in a `submition log`
   - the QASM_code data will be extracted and sent through the first part of the preprocessing stage where it will be converted to QUA code
   - h_score will be used in the log to identify the computational complexity of the algorithm/circuit, `metrics for this TBD`, may use for task queing purposes

 2. 
     
