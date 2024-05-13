import random


data = input("Enter your password : ").lower()
bias = 26
base = "a"

def encryptionRotationTwoCipher(data,bias,base,groupsCount=2):
    if 26 / groupsCount < 2 or 26 % groupsCount != 0:
        print("-Grouping is invaild!")
        return None
    
    group = [[] for i in range(groupsCount)]
    
    base = ord(base)

    alls = [itr + base for itr in range(bias)]
    allCount = len(alls)

    for item in range(allCount):
        ran = random.choice(alls)
        alls.remove(ran)
        if item % 2 == 0:
            group[0].append(ran)
        else:
            group[1].append(ran)

    cipher = ""

    for item in data:
        asci = ord(item)
        if asci in group[0]:
            num = group[0].index(asci)
            cipher += chr(group[1][num])
        else:
            num = group[1].index(asci)
            cipher += chr(group[0][num])

    return group,cipher

groups,cipher = encryptionRotationTwoCipher(data,bias,base)

for indx,iteml in enumerate(groups):
    print(f"\ngroup {indx+1} : ",end="\t")
    for item in iteml:
        print(chr(item),end="\t")

cipher = cipher if cipher != None else "-The key is invaild!"

print("\n\nCipher password :",cipher.upper())