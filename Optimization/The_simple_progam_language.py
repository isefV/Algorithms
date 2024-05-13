flg =True
while flg:
    get = [x for x in input("> ").split()]
    try:
        get += get[1].split(sep=",")
        get.remove(get[1])
        if get[0] == "ADD":
            print(int(get[1])+int(get[2])+int(get[3]))
    except :
        print("-Error!")