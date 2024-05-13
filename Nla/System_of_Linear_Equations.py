import time

def get_data(file_name):
    coe_matrix = []
    res_eq = []
    with open(file_name,'r') as file_data:
        for line in file_data:
            line_val = line.split()
            index = line_val.index('=')
            coe_matrix.append([ float(line_val[item]) for item in range(index) ])
            res_eq.append(float(line_val[-1]))
    return coe_matrix,res_eq

def backward_sle(coe_matrix,res_eq):
    unvar = []
    row_number = len(coe_matrix)
    for row in range(row_number-1,-1,-1):
        result = res_eq[row]

        for col in range(row + 1,row_number):
            result -= coe_matrix[row][col] * unvar[-(col - row)]
        
        result /= coe_matrix[row][row]

        unvar.append(result)

    unvar.reverse()
    return unvar

def forward_sle(coe_matrix,res_eq):
    unvar = []
    row_number = len(coe_matrix)
    for row in range(row_number):
        result = res_eq[row]

        for col in range(row):
            result -= coe_matrix[row][col] * unvar[col]
        
        result /= coe_matrix[row][row]

        unvar.append(result)

    return unvar


#_file_name_backward = ".\\NLO\\minimal_dataset_backward.txt"
_file_name_backward_large = ".\\NLA\\large_dataset_backward.txt"
_coe_matrix , _res_eq = get_data(_file_name_backward_large)
start_backward = time.perf_counter_ns() 
_unvar_backward = backward_sle(_coe_matrix,_res_eq)
end_backward = time.perf_counter_ns()


#_file_name_forward = ".\\NLO\\minimal_dataset_forward.txt"
_file_name_forward_large = ".\\NLA\\large_dataset_forward.txt"
_coe_matrix , _res_eq = get_data(_file_name_forward_large)
start_forward = time.perf_counter_ns() 
_unvar_forward = forward_sle(_coe_matrix,_res_eq)
end_forward = time.perf_counter_ns()


print(f"Backward Algo : {_unvar_backward}\nTime : {end_backward-start_backward} ns\n")
print(f"Forward Algo : {_unvar_forward}\nTime : {end_forward-start_forward} ns")