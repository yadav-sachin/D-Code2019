from random import *
seed(7820457)
T=10
print(T)
for t in range(T):
    if t<=3:
        if t==0:
            N, M=45,49
        if t==1:
            N,M=47,46
        if t==2:
            N,M=50,49
        if t==3:
            N,M=49,50
        arr1=[i%2 for i in range(M)]
        arr2=[1]+arr1[0:M-1]
        arr=(arr1+arr2)*(N//2)
        if N%2==1:
            arr=arr+arr1
    if 4<=t<=5:
        N, M=randint(45,50),randint(45,50)
        arr1=[ 1 if i%3 else 0 for i in range(M)]
        arr2=[1]+arr1[0:M-1]
        arr3=[1]+arr2[0:M-1]
        arr=(arr1+arr2+arr3)*(N//3)
        if N%3==1:
            arr=arr+arr1
        elif N%3==2:
            arr=arr+arr1+arr2
    if 6<=t<=8:
        #staggered 1110 and 
        N, M=randint(45,50),randint(45,50)
        arr1=[0 if i%4==0 else 1 for i in range(M)]
        arr2=[1]+arr1[0:M-1]
        arr3=[1]+arr2[0:M-1]
        arr4=[1]+arr3[0:M-1]
        arr=(arr1+arr2+arr3+arr4)*(N//4)
        if N%4==1:
            arr=arr+arr1
        elif N%4==2:
            arr=arr+arr1+arr2
        elif N%4==3:
            arr=arr+arr1+arr2+arr3
    if t==9:
        #lower half triangle is 0
        N,M=50,50
        arr=[]
        for i in range(N):
            arr=arr+[0]*i + [1]*(M-i)
    print(N,M)
    for x in range(N):
        print(*[arr[x*M+y] for y in range(M)])