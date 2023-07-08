import sys 
import re                                                                                                                                  


def read_file(filename):                                                                                                                     
     lines = []                                                                                                                               
                                                                                                                                         
     with open(filename, 'r') as file:                                                                                                        
         for line in file:                                                                                                                    
             line = line.strip() 
             if line:                                                                                                             
                lines.append(line)                                                                                                               
                                                                                                                                              
     return (lines)                                                                                                                            
                                                                                                                                             
def line_parse(line, save_list):                                                                                                                        
     elements = line.split()                                                                                                        
    
     function_name = elements[0]                                                                                                              
     function_args = elements[1:]                                                                                                          
                                                                                                                                              
     if function_name == 'qreg':                                                                                                              
         qreg(function_args)                                                                                                                  
     elif function_name == 'creg':                                                                                                            
         creg(function_args)
         cooldown()                                                                                                                  
     elif function_name == 'h':                                                                                                               
         h(function_args)                                                                                                                     
     elif function_name == 'cx':                                                                                                              
         cx(function_args)                                                                                                                   
     elif function_name == 'measure':                                                                                                         
         save_list = measure_t(function_args, save_list)  
     elif function_name == 'barrier':
         barrier(function_args) 
     elif function_name == 'x':
         x(function_args)
     elif function_name == 'sx':
         sx(function_args)
     elif function_name == 'sxdg':
         sxdg(function_args)
     elif function_name == 'y':
         y(function_args)
     elif function_name == 'z':
         z(function_args)                                                                                                      
     else:                                                                                                                                    
         print(f"Function {function_name} not found!")    
     return save_list                                                                               
                                                                                                                                              
def qreg(args):                                                                                                                              
     match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
     if match:                                                                                                                                
         qubits = int(match.group(1))
         print("from qm.qua import *")
         print("class MyClass:")
         print("\tdef QUA(iv):")
         print()
         print("\t with program() as output:") #start qua
         print("\t\t\tn = declare(int)")
         print("\t\t\tt = declare(int)")
                                                                                                                                              
def creg(args): 
    match = re.search(r'c\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1))                                                                                                
         for i in range(1, qubits+1):                                                                                                                  
            print(f"\t\t\tI{i}_st = declare_stream()")
         for i in range(1, qubits+1):                                                                                                                  
            print(f"\t\t\tQ{i}_st = declare_stream()")
         for i in range(1, qubits+1):                                                                                                                  
            print(f"\t\t\tI{i} = declare(fixed)")  
         for i in range(1, qubits+1):                                                                                                                  
            print(f"\t\t\tQ{i} = declare(fixed)")    
         print()
         print("\t\t\twith for_(n, 1, n < 10000, n ):")  # shots(loop)


def cooldown():
         print("\t\t\t\tcooldown(active_reset = active_reset)")                                                                                                                                  
                                                                                                                                                
def h(args): 
    match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1)) + 1
         print(f"\t\t\t\tHadamard(\"q{qubits}\")")                                                                                                                   
                                                                                                                                          
def cx(args):   
    pattern = r'q\[(\d+)\]'

    q_c_match = re.match(pattern, args[0])  
    q_t_match = re.match(pattern, args[1]) 

    q_c = int(q_c_match.group(1)) +1
    q_t = int(q_t_match.group(1))  +1

    print(f"\t\t\t\tCNOT_macro(\"q{q_c}\", \"q{q_t}\")") 

def x(args):
    match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1)) + 1
         print(f"\t\t\t\tX(\"q{qubits}\")")

def sx(args):
    match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1)) + 1
         print(f"\t\t\t\tXby2(\"q{qubits}\")")

def sxdg(args):
    match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1)) + 1
         print(f"\t\t\t\tmXby2(\"q{qubits}\")")

def y(args):
    match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1)) + 1
         print(f"\t\t\t\tY(\"q{qubits}\")")

def z(args):
    match = re.search(r'q\[(\d+)\]', args[0])                                                                                         
    if match:                                                                                                                                
         qubits = int(match.group(1)) + 1
         print(f"\t\t\t\tZ(\"q{qubits}\")")

def barrier(args):
    pattern = r'q\[(\d+)\]'

    q_c_match = re.match(pattern, args[0])  
    q_t_match = re.match(pattern, args[1]) 

    q_c = int(q_c_match.group(1)) +1
    q_t = int(q_t_match.group(1)) +1

    print(f"\t\t\t\talign(\"q{q_c}\", \"q{q_t}\")")

def measure_t(args, save_list): 
   
   q_list = []
   c_list = []
   
   pattern0 = r'q\[(\d+)\]'
   pattern1 = r'c\[(\d+)\]'

   q_reg_match = re.match(pattern0, args[0])  
   c_reg_match = re.match(pattern1, args[2]) 

   q_reg = int(q_reg_match.group(1)) +1
   c_reg = int(c_reg_match.group(1)) +1

   q_reg_pre = int(q_reg_match.group(1))
   c_reg_pre = int(c_reg_match.group(1))

   q_list.append(q_reg)
   c_list.append(c_reg)

   if len(c_list) > 1 :

        q_list_pre = q_list[len(q_list)]
        c_list_pre = c_list[len(c_list)]

        if (c_reg_pre == c_list_pre):
            print(f"\t\t\t\talign(\"q{q_reg_pre}\", \"rr{q_reg}\")")
            print(f"\t\t\t\tmeasure(\"readout\", \"rr{q_reg}\", None, demod.full(\"integW_cos\", I{c_reg}, adc_mapping[\"rr{q_reg}\"]), demod.full(\"integW_minus_sin\", Q{c_reg}, adc_mapping[\"rr{q_reg}\"]))")                                                                                                                      
            save_c = f"\t\t\t\tsave(I{q_reg}, I{c_reg}_st)"
            save_q = f"\t\t\t\tsave(Q{q_reg}, Q{c_reg}_st)"
            save_list.append(save_c)
            save_list1.append(save_q)
            print(f"\t\t\t\talign(\"q{q_reg_pre}\", \"rr{q_reg}\")")
        else:
                print(f"\t\t\t\talign(\"q{q_reg}\", \"rr{q_reg}\")")
                print(f"\t\t\t\tmeasure(\"readout\", \"rr{q_reg}\", None, demod.full(\"integW_cos\", I{c_reg}, adc_mapping[\"rr{q_reg}\"]), demod.full(\"integW_minus_sin\", Q{c_reg}, adc_mapping[\"rr{q_reg}\"]))")                                                                                                                        
                save_c = f"\t\t\t\tsave(I{q_reg}, I{c_reg}_st)"
                save_q = f"\t\t\t\tsave(Q{q_reg}, Q{c_reg}_st)"
                save_list.append(save_c)
                save_list1.append(save_q)
                print(f"\t\t\t\talign(\"q{q_reg}\", \"rr{q_reg}\")")
   else:
        print(f"\t\t\t\talign(\"q{q_reg}\", \"rr{q_reg}\")")
        print(f"\t\t\t\tmeasure(\"readout\", \"rr{q_reg}\", None, demod.full(\"integW_cos\", I{c_reg}, adc_mapping[\"rr{q_reg}\"]), demod.full(\"integW_minus_sin\", Q{c_reg}, adc_mapping[\"rr{q_reg}\"]))")                                                                                                                        
        save_c = f"\t\t\t\tsave(I{q_reg}, I{c_reg}_st)"
        save_q = f"\t\t\t\tsave(Q{q_reg}, Q{c_reg}_st)"
        save_list.append(save_c)
        save_list1.append(save_q)
        print(f"\t\t\t\talign(\"q{q_reg}\", \"rr{q_reg}\")")    
   return save_list

def stream_processing(save_list):
  for i in range(0, len(save_list)):
      print(save_list[i])
  print()
  print("\t\t\twith stream_processing():")
  for i in range(1, len(save_list)):                                                                                                                  
            print(f"\t\t\t\tI{i}_st.average().save(\"I{i}\")")
  for i in range(1, len(save_list)):                                                                                                                  
            print(f"\t\t\t\tQ{i}_st.average().save(\"Q{i}\")")




if len(sys.argv) == 2:                                                                                                                       
     filename = sys.argv[1]                                                                                                                   
     file_lines = read_file(filename)
     file_lines.append("GG")                                                                                                         

     save_list=[]                                                                                                                                        
     for line in file_lines:  
              if line == "GG":
                  stream_processing(save_list)
              else:                                                                                                                
               save_list  = line_parse(line, save_list)                                                                                                           
               #  execute_function(elements)                                                                                                        
else:                                                                                                                                        
     print("Please provide a filename as a command-line argument.")  
 
