import random

file_name_backward = ".\\NLA\\large_dataset_backward.txt"
file_name_forward = ".\\NLA\\large_dataset_forward.txt"
matrix_size = 10
matrix = []
res = []

with open(file_name_backward,'w') as file_data:
    for row in range(matrix_size):
        row_eq = []
        for col in range(matrix_size):
            if row > col:
                row_eq.append(0)
                file_data.write('0\t')
            else:
                ran = random.randint(1,100)
                file_data.write(f'{ran}\t')
                row_eq.append(ran)
        res.append(random.randint(50,200))
        file_data.write(f'=\t{res[row]}\n')
        matrix.append(row_eq)
        print(row_eq)

print('\n\n')

with open(file_name_forward,'w') as file_data:
    for row in range(matrix_size-1,-1,-1):
        row_eq = []
        for col in range(matrix_size-1,-1,-1):
            file_data.write(f'{matrix[row][col]}\t')

        file_data.write(f'=\t{res[row]}\n')
