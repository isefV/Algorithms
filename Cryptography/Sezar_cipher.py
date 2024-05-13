data = input("Enter your password : ").lower()
key = int(input("Enter your key : "))
bias = 26
base = ord('a')

def encryptionSezarCipher(data,key,alphaBias,base):
    cipher = ""
    for item in data:
        cipher += chr( ( (ord(item) - base + key) % alphaBias) + base)
    return cipher


def decryptionSezarCipher(data,alphaBias,base):
    decipher_list = []
    key = 0
    while key < 26 :
        decipher = ""
        for item in data:
            decipher += chr( ( (ord(item) - base - key) % alphaBias) + base)
        decipher_list.append(decipher.upper())
        key += 1
    return decipher_list

cipher = encryptionSezarCipher(data,key,bias,base)
print("Cipher password : ",cipher.upper())
decipher = decryptionSezarCipher(cipher,bias,base)
print("Decipher password : \n",decipher,"\nMy password is in Deciphers passwords : ", data.upper() in decipher,",\t", decipher[decipher.index(data.upper())])

