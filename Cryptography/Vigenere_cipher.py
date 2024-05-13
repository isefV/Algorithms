data = input("Enter your password : ").lower()
key = input("Enter your key : ").lower()
base = ord('a')


def keylengthToData(data,key):
    newKey = ""
    for ix in range(len(data)):
        newKey += key[ix%len(key)]
    return newKey

def encryptionVigenere(data,key,base):
    cipher = ""
    for i in range(len(data)):
        c = (((ord(data[i]) - base) + (ord(key[i]) - base)) % 26) + base
        cipher += chr(c)

    return cipher

key = keylengthToData(data,key)
cipher = encryptionVigenere(data,key,base)

print("Cipher password : ",cipher.upper())