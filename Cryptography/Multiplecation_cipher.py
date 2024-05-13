import math

data = input("Enter your password : ").lower()
bias = 26
base = ord('a')

def encryptionMultiCipher(data,key,alphaBias,base):
    cipher = ""

    if math.gcd(key,alphaBias) != 1:
        return None
    
    for item in data:
        cipher += chr( ( ((ord(item) - base) * key) % alphaBias) + base)

    return cipher


cipher = encryptionMultiCipher(data,3,bias,base)
cipher = cipher if cipher != None else "-The key is invaild!"
print("Cipher password : ",cipher.upper())