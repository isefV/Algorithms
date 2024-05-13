def getMatrix():
    matxCount = int(input("Enter a number of Matrix: "))
    matxRelations = []
    for i in range(matxCount):
        print(f"Enter row and column of matriz {i+1} : ")
        temp = [int(x) for x in input().split()]

        if len(matxRelations)!=0 and matxRelations[-1]==temp[0]:
            matxRelations.append(temp[1])
        else:
            matxRelations.append(temp[0])
            matxRelations.append(temp[1])

    return matxCount,matxRelations

with open("MatrixMul.txt",mode="w") as file_data:
    def lowMulMatx(matxCnt,matxRel):
        m_matx = [[ 0 for i in range(matxCnt)] for j in range(matxCnt)]

        file_data.write(f"Number of Matrix : {matxCnt}\n")
        for indx,item in enumerate(matxRel):
            file_data.write(f"d{indx} = {item}\t")
        

        for p in range(1,matxCnt):
            file_data.write(f"\nDiameter {p}:\n")
            for i,j in zip(range(matxCnt-1),range(p,matxCnt)):
                if i < j :
                    tmp_ij = []
                    file_data.write(f"M[{i+1}][{j+1}] = min {i+1} <= k <= {j} [ ")
                    for k in range(i,j):                           # matxRel[k-i]
                        tmp_ij.append(m_matx[i][k]+m_matx[k+1][j]+ (matxRel[i-1]*matxRel[k+1]*matxRel[j+1]))
                        file_data.write(f"( {m_matx[i][k]} + {m_matx[k+1][j]} + ( {matxRel[i-1]} * {matxRel[k+1]} * {matxRel[j+1]} ) ),")
                        
                    m_matx[i][j] = min(tmp_ij)
                    file_data.write(f" ] = {m_matx[i][j]}\n")
                else:
                    m_matx[i][j] = 0

                    
        return m_matx

    num,matx = getMatrix()
    m_Matrix = lowMulMatx(num,matx)

    file_data.write(f"Shape of Matrix : \n")
    for j in range(num):
        file_data.write(f"\t {j+1}")
    
    file_data.write(f"\n")
    for j in range(num+1):
        file_data.write(f"-------")
    file_data.write(f"\n")
    for i in range(num):
        file_data.write(f"{i+1}\t")
        for j in range(num):
            file_data.write(f"{m_Matrix[i][j]}\t")
            print(m_Matrix[i][j],end="\t")
        file_data.write(f"\n")
        print()
    
    print("Successful!")