import math

# top = int(input("Enter Size of batch : "))

# batch = [int(x) for x in input("Enter batches : ").split()]

# print("------------------\n")

top = 5 #20 
counter = top
batch = [4,1] #[10 ,10]

mainH = 0 
for x in batch:
    mainH += round((-x/top) * math.log2(x/top),3)


batchH = []
index = 0

while counter != 0 :
    batchH.append(0)
    batchSize = int(input("Enter Size of batches : "))

    batch = [int(x) for x in input("Enter batches : ").split()]

    for x in batch:
        if x == 0:
            continue
        batchH[index] += round((-x/batchSize) * math.log2(x/batchSize),3)

    batchH[index] = batchH[index] * (batchSize/top)

    print(f"{index + 1} : {batchH[index]}")
    counter -= batchSize
    index += 1

print(f"\nsum : {sum(batchH)} & {1 - sum(batchH)}")

# print(f"Benfit :")
# index = 1
# for x in batchH:
#     print(f"H {index} : {1-x}")

