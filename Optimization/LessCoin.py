LeastCoin = []
c = 15
unitCoins = [1,3,6,10]
LeastCoin.append(0)
for m in range(1,c+1):
    LeastCoin.append(1000)
    for v in unitCoins:
        print(f"m = {m}\tv = {v}\t <= {LeastCoin[m]}",end='\t\t')
        if v <= m and LeastCoin[m-v] + 1 <= LeastCoin[m]:
            print(f"v <= m\t\tM[ {m} - {v} ] + 1 ~ {LeastCoin[m-v]} <= M[ {m} ] ~ {LeastCoin[m]}",end='\t')
            LeastCoin[m] = LeastCoin[m-v] + 1
            print(f"===>\tM[{m}] = {LeastCoin[m-v] + 1}")
        else:
            print(f"v >  m\t")

print(LeastCoin)
