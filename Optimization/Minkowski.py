import numpy as np

def getn():
    r = int(input("Enter r :"))
    n = int(input("Enter number of row : "))
    rows = [[int(x) for x in input(f"Enter Features of obj {i+1} : ").split()]for i in range(n)]
    return r,rows

def minkowski(r,rows):
    dist = [[0 for i in range(len(rows))] for i in range(len(rows))]
    for ii,i in enumerate(rows):
        for ij,j in enumerate(rows):
            if ii == ij:
                continue
            
            arr_1 = np.array(i)
            arr_2 = np.array(j)
            print(f"\nr {ii} , c {ij}")
            dif = arr_1 - arr_2
            dif = np.abs(dif)
            print("diff : ",dif)
            power = np.power(dif,r)
            print("power : ",power)
            res = np.sum(power)
            print("sum : ",res)
            dist[ii][ij] = round(np.cbrt(res),2)
    return dist

r,data = getn()
print("Result is : \n",minkowski(r,data))

