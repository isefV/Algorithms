def Jacobi(eq,val,x_k,iter):
    print("+ Jacobi Algo :")
    for iter in range(iter):
        upadate_x_k = []
        for index_i in range(len(eq)):
            result = val[index_i]
            for index_j in range(len(eq)):
                if index_i == index_j:
                    continue
                result -= eq[index_i][index_j] * x_k[index_j]
            result =  result / eq[index_i][index_i]
            upadate_x_k.append(result)

        x_k = upadate_x_k.copy()
        print(f"\t| Iterations {iter} : ",*x_k)

def Gauss_Seidel(eq,val,x_k,iter):
    print("+ Gauss Seidel Algo :")
    for iter in range(iter):
        update_x_k = []
        for index_i in range(len(eq)):
            result = val[index_i]
            for index_j in range(len(eq)):
                if index_i == index_j:
                    continue

                if index_j > index_i:
                    result -= eq[index_i][index_j] * x_k[index_j]
                else:
                    result -= eq[index_i][index_j] * update_x_k[index_j]
            result =  result / eq[index_i][index_i]
            update_x_k.append(result)

        x_k = update_x_k.copy()
        print(f"\t| Iterations {iter} : ",*x_k)

def SOR(eq,val,x_k,iter):
    print("+ SOR Algo :")
    w = float(input(" - Enter The Wieght [0,1] : "))
    w_c = 1 - w
    temp_w = w if w != 0 else 1
    for index in range(len(eq)):
        if eq[index][index] == 0:
            print("The main diameter is zero.")
            break

    for iter in range(iter):
        upadate_x_k = []
        for index_i in range(len(eq)):
            result = val[index_i]
            for index_j in range(len(eq)):
                if index_i == index_j:
                    continue
                elif index_i > index_j:
                    result -= eq[index_i][index_j] * upadate_x_k[index_j]
                else:
                    result -= eq[index_i][index_j] * x_k[index_j]
            result =  result * ( temp_w / eq[index_i][index_i])
            result =  result + (w_c * x_k[index_i])
            upadate_x_k.append(result)

        x_k = upadate_x_k.copy()
        print(f"\t| Iterations {iter} : ",*x_k)
    if w == 1 :
        print("\tLike Gauss-Seidel method.")
    elif w == 0 :
        print("\tLike Jacobi method.")
    elif w > 1:
        print("\tOver-Relaxation.")
    else:
        print("\tUnder-Relaxation.")