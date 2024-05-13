nGroup = int(input("The number of group : "))
weightGroup = [int(x) for x in input(f"The weight of 1-{nGroup} : ").split()]
finalWeight = int(input("The final  weight : "))

_result = []

def promis(number,arr):
    temp = number
    for i in arr:
        temp -= i
    if temp == 0:
        return True
    return False

step = 0

def recSubset(stp):
    
    if promis(finalWeight,_result):
        return True
    for item in weightGroup:
        if item in _result:
            continue
        _result.append(item)
        print(f"Step : {stp + 1} / ",end=' ')
        if recSubset(stp + 1):
            print(f" Step : {stp + 1} , item {item}: {_result}")
            return True
        _result.pop()
        print(f"Step : {stp + 1} , item {item}: {_result} ." )
        
    return False


print(recSubset(step),_result)