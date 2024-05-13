import random

data = input("Enter your password : ").lower()
bias = 26
base = ord('a')
alphaCipher = [ i + base for i in range(bias)]


def searchInMatrix(item,matrix):
    row_i,col_i=0,0

    for row in matrix:
        for col in row:
            if item == col:
                return row_i,col_i
            col_i+=1
        col_i = 0
        row_i+=1
    return None,None

def circleInMatrix(num,dimen):
    if num < dimen :
        return num
    return num % dimen


def makeKeyMatrix(alphaCipher,rows=5,column=5):
    matrix = []
    j_word = 106
    alphaCipher.remove(j_word)

    for r in range(rows):
        row = []
        for c in range(column):
            if len(alphaCipher) != 0:
                ran = random.choice(alphaCipher)
                alphaCipher.remove(ran)
            else:
                ran = 45
            row.append(ran)
        matrix.append(row)
    return matrix

def makeSentList(data):
    digraphs = []
    temp_ch = ""
    for ch in data:
        if len(temp_ch) < 2:
            if temp_ch != ch:
                temp_ch += ch
            else:
                temp_ch += "x"
                digraphs.append(temp_ch)
                temp_ch = ch
        else:
            digraphs.append(temp_ch)
            temp_ch = ch
    if len(temp_ch) == 1:
        temp_ch += "z"
    digraphs.append(temp_ch)
    return digraphs
            
def bicharTomtrix(digraph,matrix):

    cipher = ""
    rowSize = len(matrix)
    colSize = len(matrix[0])

    for bitem in digraph:
        left,right = bitem[0],bitem[1]
        oleft,oright = ord(left),ord(right)


        # for pair have 'j' we except to been own letters
        if left == "j" or right == "j":
            cipher += left
            cipher += right
            continue

        li,lj = searchInMatrix(oleft,matrix)
        ri,rj = searchInMatrix(oright,matrix)

        if li == ri:
            cipher += chr(matrix[li][circleInMatrix(lj+1,colSize)])
            cipher += chr(matrix[ri][circleInMatrix(rj+1,colSize)])
        elif lj == rj:
            cipher += chr(matrix[circleInMatrix(li-1,rowSize)][lj])
            cipher += chr(matrix[circleInMatrix(ri-1,rowSize)][rj])
        else:
            li,ri = ri,li
            cipher += chr(matrix[li][lj])
            cipher += chr(matrix[ri][rj])
        
    return cipher

def encryptionPlayfair(data):
    data_list = makeSentList(data)
    print("Token list : ",data_list)


    key = makeKeyMatrix(alphaCipher)
    print("Key matrix :\n")
    for i in key:
        print("\t")
        for j in i:
            print(chr(j),end="\t")
        
        

    cipher = bicharTomtrix(data_list,key)
    print("\n\nCipher password : ",cipher.upper())
    return cipher

encryptionPlayfair(data)