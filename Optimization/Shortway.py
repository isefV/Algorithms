def getGraphDescrib():
    nodeCount = int(input("Enter a number of Nodes: "))
    nodeRelations = []
    for i in range(nodeCount):
        print(f"Enter Relations of V0 V1 ... V{nodeCount-1} by V{i} (for infinit set .): ")
        temp = [x if x=='.' else int(x) for x in input().split()]
        for j in range(len(temp)):
            if i == j:
                temp[i] = 0 
        nodeRelations.append(temp)
    return nodeCount,nodeRelations

with open("ShortWay.txt",mode="w") as file_data:
    def shortWay(nodeCnt,nodeRel,opstion=0):
        d_tbl = [nodeRel]
        zero = [[0]*nodeCnt]*nodeCnt
        p_tbl = [zero]

        for i in range(1,nodeCnt+1):
            nd_tbl = []
            np_tbl = []

            file_data.write(f"\nCalculation of table {i} :\n")

            for j in range(nodeCnt):
                nd_row = []
                np_row = []
                for k in range(nodeCnt):
                    
                    flg_infi = [(d_tbl[i-1][j][k] != '.') , d_tbl[i-1][j][i-1] != '.' and d_tbl[i-1][i-1][k]!='.']
                    #file_data.write(f"Number of Matrix : {matxCnt}\n")

                    if  all(flg_infi):
                        d_temp = min(d_tbl[i-1][j][k] , d_tbl[i-1][j][i-1] + d_tbl[i-1][i-1][k])

                        file_data.write(f"D-{i} [{j+1}][{k+1}] = min [ {d_tbl[i-1][j][k]} , ( {d_tbl[i-1][j][i-1]} + {d_tbl[i-1][i-1][k]} ) ] = {d_temp}\n")
                        
                        if d_temp == d_tbl[i-1][j][k]:
                            p_temp = p_tbl[i-1][j][k]
                            file_data.write(f"P-{i} [{j+1}][{k+1}] = {p_temp}\n")
                        else:
                            p_temp = i
                            file_data.write(f"P-{i} [{j+1}][{k+1}] = {p_temp}\n")

                    elif  flg_infi[0]:
                        d_temp = d_tbl[i-1][j][k]
                        file_data.write(f"D-{i} [{j+1}][{k+1}] = min [ {d_temp} , infinite ] = {d_temp}\n")
                        p_temp = p_tbl[i-1][j][k]
                        file_data.write(f"P-{i} [{j+1}][{k+1}] = {p_temp}\n")

                    elif flg_infi[1]:
                        d_temp =  d_tbl[i-1][j][i-1] + d_tbl[i-1][i-1][k]
                        file_data.write(f"D-{i} [{j+1}][{k+1}] = min [ infinite , {d_temp}  ] = {d_temp}\n")
                        p_temp = i
                        file_data.write(f"P-{i} [{j+1}][{k+1}] = {p_temp}\n")
                    else:
                        d_temp = '.'
                        file_data.write(f"D-{i} [{j+1}][{k+1}] = min [ infinite , infinite ] = infinite\n")
                        p_temp = 0       
                        file_data.write(f"P-{i} [{j+1}][{k+1}] = {p_temp}\n")

                    file_data.write(f"\n")

                    nd_row.append(d_temp)
                    np_row.append(p_temp)
                nd_tbl.append(nd_row)
                np_tbl.append(np_row)
            d_tbl.append(nd_tbl)
            p_tbl.append(np_tbl)

        file_data.write(f"\nMatrix of D & P table :\n")

        if opstion == 0:
            print("----------\n","D table:")
            for i in range(nodeCnt):
                for j in range(nodeCnt):
                    print(d_tbl[nodeCnt][i][j],end="\t")
                print()
            print("\nP table:")
            for i in range(nodeCnt):
                for j in range(nodeCnt):
                    print(p_tbl[nodeCnt][i][j],end="\t")
                print()
            print("----------\n")
                
        elif opstion == 1 :
            for k in range(nodeCnt+1):
                file_data.write(f"\n\t\t----- D-{k} table -----\t\t\n\t")
                print("----------\n",f"D{k} table:")
                for n in range(nodeCnt):
                    file_data.write(f"{n+1}\t")
                for i in range(nodeCnt):
                    file_data.write(f"\n{i+1}|\t")
                    for j in range(nodeCnt):
                        print(d_tbl[k][i][j],end="\t")
                        file_data.write(f"{d_tbl[k][i][j]}\t")
                    print()
                
                file_data.write(f"\n\t\t----- P-{k} table -----\t\t\n\t")
                print(f"\nP{k} table:")
                for n in range(nodeCnt):
                    file_data.write(f"{n+1}\t")
                for i in range(nodeCnt):
                    file_data.write(f"\n{i+1}|\t")
                    for j in range(nodeCnt):
                        print(p_tbl[k][i][j],end="\t")
                        file_data.write(f"{p_tbl[k][i][j]}\t")
                    print()
                print("----------\n")
        return True

    data = getGraphDescrib()
    shortWay(data[0],data[1],1)

    print("Successful!")