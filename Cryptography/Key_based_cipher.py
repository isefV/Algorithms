import random

data = input("Enter your password : ").lower()
size = 5

def makeTokenData(data,size):
    token = []
    temp_ch = ""
    for ch in data:
        if len(temp_ch) >= 5:
            token.append(temp_ch)
            temp_ch = ch
            continue
        
        temp_ch += ch
    
    temp_ch +=  "z" * (size - len(temp_ch))
    token.append(temp_ch)
    return token

def bijection(size):
    matchMap = []
    des = [ i for i in range(size)]
    for i in range(size):
        ran = random.choice(des)
        matchMap.append(ran)
        des.remove(ran)

    return matchMap

def moveletters(word,keyd,size):
    nword = [" " for i in  range(size)]
    for i,v in enumerate(keyd):
        nword[v] = word[i]
    c = ''
    for i in nword:
        c+=i
    return c

def encryptionKeyBased(data,keyd):
    cipher = ""
    for item in data:
        cipher += moveletters(item,keyd,len(item))
    return cipher

dataToken = makeTokenData(data,size)
key = bijection(size)
cipher = encryptionKeyBased(dataToken,key)

print("Cipher password : ",cipher.upper())

