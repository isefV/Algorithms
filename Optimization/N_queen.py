dimen = 4
n_queen = 4
_queens = []


def promis(queens,i,j):
    for item in queens:
        if item[0] == i:
            return False
        elif item[1] == j:
            return False
        elif abs(item[0]-i) == abs(item[1]-j):
            return False
    return True


def recQueen(row):
    if row >= dimen:
        return True
    for col in range(dimen):
        if promis(_queens,row,col):
            _queens.append([row,col])
            if recQueen(row + 1):
                return True
            _queens.pop()
    return False


print(recQueen(0),_queens)