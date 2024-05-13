# job = [int(x) for x in input("Enter job list : ").split()]
# time = [int(x) for x in input("Enter time job list : ").split()]
# cost = [int(x) for x in input("Enter cost job list : ").split()]

job = [1 ,2, 3, 4, 5, 6, 7]
time = [2 ,4, 3, 2 ,3, 1, 1]
cost = [40 ,15 ,60 ,20 ,10 ,45 ,55]

# job = [1 ,2, 3, 4, 5, 6, 7]
# time = [3,1,1,3,1,3,2]
# cost = [40,35,30,25,20,15,10]

def makePairs(job,time,cost):
    tb = {}
    for index in range(len(job)):
        tb[cost[index]] = [job[index],time[index]]
    return tb

def sortDict(dicts):
    return dict(sorted(dicts.items(),  reverse = True))


def check(choice):
    time_l = {}
    for key,val in choice.items():
        time_l[val[0]] = val[1]
    time_l = dict(sorted(time_l.items(), key=lambda item: item[1])) 
    for i,v in enumerate(time_l):
        if i <= time_l[v]-1 :
            continue
        return False
    return True


def scheduling(data):
    total = {}
    for key,val in data.items():
        print(f"{key} : {val}",end="\t")
        total[key] = val
        if check(total):
            print(total)
            continue
        
        total.pop(key)
        print(total)

    return total

x = makePairs(job,time,cost)
y = sortDict(x)
print(x,"\n",y)
print(scheduling(y))

