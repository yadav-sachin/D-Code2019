from random import *
seed(224982489690869)
T=5
print(T)
for t in range(T):
    N=10**5
    if t==0:
        #99990
        N=99991
        arr=list(range(1,30))*3333 + [29] + list(range(1,31))*3333
    if t==1:
        N-=1
        arr=[]
        while len(arr)<49999:
            m=randint(1,30)
            i=1
            while(m*i<=30):
                arr.append(m*i)
                i+=1
        arr2=arr
        arr.append((arr[-1]+1)%30+1)
        arr+=arr2
    if t==2:
        N-=1
        arr=[]
        while len(arr)<49999:
            m=randint(1,30)
            i=1
            while(m*i<=30):
                arr.append(m*i)
                i+=1
        arr2=arr
        arr.append((arr[-1]+1)%30+1)
        arr+=arr2[::-1]
    if t==3:
        N-=1
        arr=[]
        while len(arr)<49999:
            m=randint(1,30)
            i=1
            while(m*i<=30):
                arr.append(m*i)
                i+=1
        axe=randint(500,10000)
        arr=arr[axe:] + arr[ :axe]
        arr2=arr[::-1]
        axe=randint(500,10000)
        arr2=arr2[axe:]+arr2[ :axe]
        arr.append((arr[-1]+1)%30+1)
        arr+=arr2
    if t==4:
        N-=1
        arr=[]
        while len(arr)<49999:
            m=randint(1,30)
            i=1
            while(m*i<=30):
                arr.append(m*i)
                i+=1
        for g in range(10):
            axe=randint(500,10000)
            arr=arr[axe:] + arr[ :axe]
        arr2=arr[::-1]
        for h in range(10):
            axe=randint(500,10000)
            arr2=arr2[axe:] + arr2[ :axe]
        arr.append((arr[-1]+1)%30+1)
        arr+=arr2[::-1]
    print(N)
    arr=[randint(1,30) for i in range(N)]
    print(*arr)