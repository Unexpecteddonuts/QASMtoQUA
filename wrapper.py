from qm.QuantumMachinesManager import QuantumMachinesManager
from configuration_4qubitsv2 import *
import importlib.util
import stream_count

spec = importlib.util.spec_from_file_location("code", "./QUA.py")
code_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(code_module)

qubits = stream_count()

##################################
#         QUA _CODE_INSERT       #
##################################
instance = code_module.MyClass()
rabi = instance.QUA()

##################################
#       Execute on the OPX       #
##################################
qmm = QuantumMachinesManager()
qm = qmm.open_qm(config)
job = qm.execute(rabi)
res_handles = job.result_handles
job.result_handles.wait_for_all_values()

for i in range(1, qubits +1):

    I_name = "I" + str(i)                                                                                                                                                                                               
    Q_name = "Q" + str(i) 

    I_name = job.result_handles.get(I_name).fetch_all()                                                                                                                                         
    Q_name = job.result_handles.get(Q_name).fetch_all()       

    print(I_name, Q_name)                                                                                                                                                                                     
    
