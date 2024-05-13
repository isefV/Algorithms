name_of_process=[]
name_of_resource=[]
count_of_each_resource=[]
allocation=[]
need=[]
maxn=[]
available=[]

def get_inputs(np,nr):
    for i in range(np):
        name_of_process.append(input("enter a name of the process:"))
    for i in range(nr):
        name_of_resource.append(input("enter a name of the resource:"))
    for i in range(nr):
        temp="enter a value of the resource " + name_of_resource[i] + " :"
        count_of_each_resource.append(int(input(temp)))
    for i in range(np):
        t=[]
        for j in range(nr):
            temp="enter a value of allocation for "+ name_of_process[i] + " and " + name_of_resource[j] + " :" 
            t.append(int(input(temp)))
        allocation.append(t)
    for i in range(np):
        t=[]
        for j in range(nr):
            temp="enter a value of max for "+ name_of_process[i] + " and " + name_of_resource[j] + " :" 
            t.append(int(input(temp)))
        maxn.append(t)

def cal_need_avail(np,nr):
    for i in range(np):
        t=[]
        for j in range(nr):
            sub = maxn[i][j] - allocation[i][j]
            t.append(sub)
        need.append(t) 
    temp=[0 for x in range(nr)]
    for i in range(np):
        for j in range(nr):
            temp[j]+=allocation[i][j]
    for j in range(nr):
        available.append(count_of_each_resource[j]-temp[j])
    
    f = [0]*np
    ans = [0]*np
    ind = 0
    for k in range(np):
        f[k] = 0
        
    y = 0
    for k in range(np):
        for i in range(np):
            if (f[i] == 0):
                flag = 0
                for j in range(nr):
                    if (need[i][j] > available[j]):
                        flag = 1
                        break
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(nr):
                        available[y] += allocation[i][y]
                    f[i] = 1
                    
    print("Following is the SAFE Sequence")
    
    for i in range(np - 1):
         print(" P", name_of_process[ans[i]], " ->", sep="", end="")
    print(" P", name_of_process[ans[np - 1]], sep="")
    

number_of_process=int(input("enter number of process:"))
number_of_resource=int(input("enter number of resource:"))

get_inputs(number_of_process,number_of_resource)
cal_need_avail(number_of_process,number_of_resource)
print(number_of_process,number_of_resource,name_of_process,name_of_resource,allocation,maxn,need,available,count_of_each_resource)