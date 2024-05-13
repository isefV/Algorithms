import numpy as np


# methods defined

def displayCyclotomicCosets(c,g,n,mod):
    print(f"\nConsider the cyclotomic cosets of {n} modulo {mod} :")
    for index,item in zip(g,c):
        print(f"C-{index} : {item}")
    print(f"\nGroups C-i the same cyclotomic cosets :")
    for key,val in g.items():
        print(f"Group C-{key} : {val}")

def displayMinmalStr(m,q,qm):
    print(f"\nMin Polynomial F-{qm} over F-{q} :")
    for index,val in enumerate(m):
        print(f"m-{index} : {val}")

def findIndexSameItem(item,lists,group):
    for g,v in zip(group,lists):
        if item == v:
            return g
    return -1

def cyclotomicCosets(n = 2,mod = 15,max_size=10):
    max_size = (mod % 10) * 10
    c = np.array([[ -1 for j in range(max_size)] for i in range(max_size)]) 
    for index in range(c.shape[0]):
        repeat = True
        power = 0
        inner_index = 0
        while repeat:
            temp = (index * (n**power)) % mod

            if temp not in c[index]:
                c[index][inner_index] = temp
                inner_index += 1
            else:
                repeat = False

            power += 1

    final_c = []
    groups_c = {}
    for index in range(c.shape[0]):
        temp = np.unique(c[index])

        temp_list = []

        for item in temp:
            if item != -1:
                temp_list.append(item)

        if temp_list not in final_c:
            final_c.append(temp_list)
            groups_c[index] = [index]
        else:
            inx = findIndexSameItem(temp_list,final_c,groups_c)
            if inx != -1:
                groups_c[inx].append(index)
    
    return final_c,groups_c

def minPolynomial(q = 2,qm = 15):
    c,g = cyclotomicCosets(q,qm-1)
    m_min = []
    for ci in c:
        m_i = ''
        for item in ci:
            m_i += f'(x - a^{item}) '
        m_min.append(m_i)
    return m_min
# main app

# cyclotomicCosets : for calculate cyclotomic cosets of N modulo X(mod)
#                    this function return Ci : list ,and Ci groups same cyclotomic cosets : dictinary
#                    the default arg is N = 2 and mod = 15
c,g = cyclotomicCosets(3,8)
displayCyclotomicCosets(c,g,3,8)


# minPolynomial : for calculate minimal polynomial of F-q^m over F-q
#                    this function return m-i : list of string formula
#                    the default arg is q = 2 and qm = 15
m = minPolynomial(3,9)
displayMinmalStr(m,3,9)