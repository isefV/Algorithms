
import math

# top = int(input("Enter whole number : "))

# batch = [int(x) for x in input("Enter batches : ").split()]

# print("------------------\n")

top = 7 #14
# group = {'s':[[3,2],[5,4]],'j':[[2,3],[7,2]],'m':[[4,0],[5,5]]}

# ginimax = .54

# group = {'z':[[2,2],[7,3]],'m':[[4,2],[5,3]],'k':[[3,1],[6,4]]}
# group = {'j':[[3,2],[6,3]],'m':[[3,1],[6,4]],'s':[[3,2],[6,4]]}
# group = {'d':[[6,1],[3,4]]}
# group = {'a':[[3,3],[6,2]]}

# group = {'j':[[2,0],[4,1]],'m':[[2,0],[4,1]],'s':[[2,1],[4,0]]}
# group = {'z':[[1,0],[5,1]],'m':[[2,0],[4,1]],'k':[[3,1],[3,0]]}
# group = {'a':[[5,0],[1,1]]}

# group = {'z':[[1,2],[2,2]],'m':[[2,2],[1,2]],'k':[[0,0],[3,4]]}
# group = {'j':[[1,2],[2,2]],'m':[[1,1],[2,3]],'s':[[1,1],[2,3]]}
group = {'a':[[2,2],[1,2]]}



for key,batch in group.items():
    gini = 0
    for x in batch:
        if sum(x) == 0:
            continue
        temp = 1-((x[0]/sum(x))**2 + (x[1]/sum(x))**2)
        temp = round((sum(x)/top) * temp,3)
        print(f"{temp}",end=" ")
        gini += temp
    print(f"= {gini}")

    



