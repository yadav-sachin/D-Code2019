def decY_incX(x,y):
    if x[1]!=y[1]:
        return y[1]-x[1]
    else :
        return x[0]-y[0]
from functools import *
from random import *
seed(73438340986886893896)
T=10
print(T)
for t in range(T):
    N=9*10**4  
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
        for i in range(100):
            idx=randint(10,len(arr)-1000)
            x,y=arr[idx][0],arr[idx][1]
            y=2*randint(1,y//2)
            x=2*randint(1,x//2)
            arr=arr[:idx] + [[x,y,randint(1,100)]] + arr[idx:]
        N+=100
        arr=arr[::-1]
    if t==2:
        #valley but a different type one
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
        axe=randint(3*N//8,5*N//8)
        arr[axe:].reverse()
        arr=arr[:axe] + arr[axe:]
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
        axe=randint(3*N//8,5*N//8)
        arr[:axe].reverse()
        arr2=arr[:axe]
        arr3=arr[axe:]
        arr=[]
        while(arr2 and arr3):
            arr.append(arr2[0])
            arr.append(arr3[0])
            arr2=arr2[1:]
            arr3=arr3[1:]
        arr+=arr2
        arr+=arr3
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
        axe=randint(3*N//8,5*N//8)
        arr[:axe].reverse()
        arr2=arr[:axe]
        arr3=arr[axe:]
        arr=[]
        while(arr2 and arr3):
            arr.append(arr3[0])
            arr.append(arr2[0])
            arr2=arr2[1:]
            arr3=arr3[1:]
        arr+=arr2
        arr+=arr3
    if t==5:
        #reverse sorted
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
        arr=arr[::-1]
    if t==6:
        #vallley
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
        axe=randint(3*N//8,5*N//8)
        arr[:axe].reverse()
        arr=arr[:axe] + arr[axe:]
    if t==7:
        #interleaved in a pattern
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
        axe=randint(3*N//8,5*N//8)
        arr[:axe].reverse()
        arr2=arr[:axe]
        arr3=arr[axe:]
        arr=[]
        while(arr2 and arr3):
            arr.append(arr2[0])
            arr.append(arr3[0])
            arr2=arr2[1:]
            arr3=arr3[1:]
        arr+=arr2
        arr+=arr3
    if t==8:
        #interleaved in patterns
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
        axe=randint(3*N//8,5*N//8)
        arr[:axe].reverse()
        arr2=arr[:axe]
        arr3=arr[axe:]
        arr=[]
        while(arr2 and arr3):
            arr.append(arr3[0])
            arr.append(arr2[0])
            arr2=arr2[1:]
            arr3=arr3[1:]
        arr+=arr3
        arr+=arr2
    if t>8:
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
    for w in arr:
        print(*w)