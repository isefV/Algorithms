import numpy as np

dim = int(input("dimension of matrix A : ")) 
mA = np.array([[int(x) for x in input(f"The Row {i} of Matrix A : ").split()] for i in range(dim)])
mB = np.array([[int(x) for x in input(f"The Row {i} of Matrix B : ").split()] for i in range(dim)])

threshold = 4
def strasen(dim,matA,matB):
    if dim < threshold:
        # print(f"\t\tFor this matrixs \n\t\t\tA : {matA}\n\t\t\tB : {matB}")
        m1 = (matA[0,0] + matA[1,1]) * (matB[0,0] + matB[1,1])
        m2 = (matA[1,0] + matA[1,1]) * matB[0,0]
        m3 = matA[0,0] * (matB[0,1] - matB[1,1])
        m4 = matA[1,1] * (matB[1,0] - matB[0,0])
        m5 = (matA[0,0] + matA[0,1]) * matB[1,1]
        m6 = (matA[1,0] - matA[0,0]) * (matB[0,0] + matB[0,1])
        m7 = (matA[0,1] - matA[1,1]) * (matB[1,0] + matB[1,1])

        # print("\nms")
        # print(f"|({m1} {m4} {m5} {m7})\t\t({m3} {m5})|")
        # print(f"|({m2} {m4})\t\t({m1} {m3} {m2} {m6})|\n")

        return np.array([[m1+m4-m5+m7,m3+m5],[m2+m4,m1+m3-m2+m6]])
    else:
        splt = (dim // 2)
        a00 = matA[0:splt,0:splt]
        a01 = matA[0:splt,splt:]
        a10 = matA[splt:,0:splt]
        a11 = matA[splt:,splt:]

        b00 = matB[0:splt,0:splt]
        b01 = matB[0:splt,splt:]
        b10 = matB[splt:,0:splt]
        b11 = matB[splt:,splt:]

        m1 = strasen(splt , a00 + a11 , b00 + b11)
        print(f"M1 : {m1}")
        m2 = strasen(splt , a10 + a11 , b00)
        print(f"M2 : {m2}")
        m3 = strasen(splt , a00 , b01 - b11)
        print(f"M3 : {m3}")
        m4 = strasen(splt , a11 , b10 - b00)
        print(f"M4 : {m4}")
        m5 = strasen(splt , a00 + a01 , b11)
        print(f"M5 : {m5}")
        m6 = strasen(splt , a10 - a00 , b00 + b01)
        print(f"M6 : {m6}")
        m7 = strasen(splt , a01 - a11 , b10 + b11)
        print(f"M7 : {m7}\n\n")

        c00 = m1+m4-m5+m7
        c01 = m3+m5
        c10 = m2+m4
        c11 = m1+m3-m2+m6

        print(f"C00 : {c00}")
        print(f"C01 : {c01}")
        print(f"C10 : {c10}")
        print(f"C11 : {c11}")

        ctop = np.concatenate((c00,c01),axis=1)
        cbottom = np.concatenate((c10,c11),axis=1)
        return np.concatenate((ctop,cbottom),axis=0)



mC = strasen(dim,mA,mB)
print("\n\nMulty:\n",mC,"\n----------------\n")
print(mA @ mB)