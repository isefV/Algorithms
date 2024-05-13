LeastCoin = [0] 
for m in range(1, M+1):
    LeastCoin.append(float('inf'))
    for i in range(1, d+1):
        if m >= C[i]:
            if LeastCoin[m - C[i]] + 1 < LeastCoin[m]:
                LeastCoin[m] = LeastCoin[m - C[i]] + 1

return LeastCoin[M] 
