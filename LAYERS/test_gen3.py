from random import *
seed(739848039860806)
T=10
print(T)
for t in range(T):
    N=8*10**4  
    C=100 
    if t==0:
        #sorted
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
    if t==1:
        #reverse sorted
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        arr.reverse();
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr=arr[::-1]
    if t==2:
        #valley
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr[:N//2].reverse()
        arr=arr[:N//2] + arr[N//2:]
    if t==3:
        #interleaved
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        for i in range(100):
            idx=randint(1,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr[:N//2].reverse()
        arr2=arr[:N//2]
        arr3=arr[N//2:]
        arr=[]
        for i in range(N//2):
            arr.append(arr2[i])
            arr.append(arr3[i])
    if t==4:
        #interleaved in differnet pattern
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        arr.reverse()
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr[:N//2].reverse()
        arr2=arr[:N//2]
        arr3=arr[N//2:]
        arr=[]
        for i in range(N//2):
            arr.append(arr3[i])
            arr.append(arr2[i])
    if t==5:
        #reverse sorted
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr=arr[::-1]
    if t==6:
        #valley
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        arr.reverse()
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr[:N//2].reverse()
        arr=arr[:N//2] + arr[N//2:]
    if t==7:
        #interleaved
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        arr.reverse()
        for i in range(100):
            idx=randint(1,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr[:N//2].reverse()
        arr2=arr[:N//2]
        arr3=arr[N//2:]
        arr=[]
        for i in range(N//2):
            arr.append(arr2[i])
            arr.append(arr3[i])
    if t>=8:
        #shuffled
        x=[2*randint(1,10**9//2) for i in range(N)]
        y=[2*randint(1,10**9//2) for i in range(N)]
        x.sort()
        y.sort(reverse=True)
        arr=[[x[i],y[i],randint(1,100)] for i in range(N)]
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        shuffle(arr)
    print(N,C)
    for b in arr:
        print(*b)