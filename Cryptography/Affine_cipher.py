import math

data = input("Enter your password : ").lower()
bias = 26
base = ord("a")
key_1 = 3
key_2 = 2

def encryptionAffineCipherAM(data,key_1,key_2,alphaBias,base):
    cipher = ""
    if math.gcd(key_1,alphaBias) != 1:
        return None
    for item in data:
        cipher += chr( ( ((ord(item) - base + key_2) * key_1) % alphaBias) + base)
    return cipher

def encryptionAffineCipherMA(data,key_1,key_2,alphaBias,base):
    cipher = ""
    if math.gcd(key_1,alphaBias) != 1:
        return None
    for item in data:
        cipher += chr( ( (((ord(item) - base ) * key_1) + key_2) % alphaBias) + base)
    return cipher


cipher_1 = encryptionAffineCipherAM(data,key_1,key_2,bias,base)
cipher_1 = cipher_1 if cipher_1 != None else "-The key is invaild!"

cipher_2 = encryptionAffineCipherMA(data,key_1,key_2,bias,base)
cipher_2 = cipher_2 if cipher_2 != None else "-The key is invaild!"

print("1-Cipher password (First add then mul): ",cipher_1.upper())
print("2-Cipher password (First mul then add): ",cipher_2.upper())