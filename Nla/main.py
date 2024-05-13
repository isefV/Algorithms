from Get_data import get_data
import Iterative_Linear_Equations_Solver_Methods as ILESM

def display(eq,val):
    for index,item in enumerate(eq):
        print("|\t",'\t'.join([str(x) for x in item]),end="\t")
        print(f"{val[index]}\t|")

eq,val = get_data(".\\Equations-3.txt")

display(eq,val)

iterations = int(input(" - Enter The Number Of Iteration : ")) + 1
x_k = [float(item) for item in input(f" - Enter {len(eq)} Values For x_0 :").split()]

for index in range(len(eq)):
    if eq[index][index] == 0:
        print("! The main diameter is zero. !")
        break

ILESM.Jacobi(eq,val,x_k,iterations)
ILESM.Gauss_Seidel(eq,val,x_k,iterations)
ILESM.SOR(eq,val,x_k,iterations)


