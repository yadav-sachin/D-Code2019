from random import *
seed(9037509175097)
T=10
print(T)
for t in range(T):
    if t==0:
        #spiral pattern around (0,0)
        M,N=50, 50
        arr=[0]*(M*N) 
        for c in range(0,N,2):
            i,j=0,c
            while i<=j:
                arr[i*M+j]=1
                i+=1
            i,j=c,0
            while j<=i:
                arr[i*M+j]=1
                j+=1
    if t==1:
        #spiral around center of board
        N,M=49,49
        arr=[0]*(M*N)
        x,y=N//2, M//2
        for c in range(1,M//2,2):
            i,j=x+c,y-c
            while j<=y+c:
                arr[i*M+j]=1
                j+=1
            i,j=x-c,y-c
            while j<=y+c:
                arr[i*M+j]=1
                j+=1
            i,j=x-c,y-c
            while i<=x+c:
                arr[i*M+j]=1
                i+=1
            i,j=x-c,y+c
            while i<=x+c:
                arr[i*M+j]=1
                i+=1
    if t==2:
        #spiral around (0,0) without diagnol corners
        M,N=50, 50
        arr=[0]*(M*N) 
        for c in range(0,N,2):
            i,j=0,c
            while i<j:
                arr[i*M+j]=1
                i+=1
            i,j=c,0
            while j<i:
                arr[i*M+j]=1
                j+=1
    if t==3:
        #spiral around center of board without diagnol corners
        N,M=49,49
        arr=[0]*(M*N)
        x,y=N//2, M//2
        for c in range(1,M//2,2):
            i,j=x+c,y-c
            while j<y+c:
                arr[i*M+j]=1
                j+=1
            i,j=x-c,y-c
            while j<y+c:
                arr[i*M+j]=1
                j+=1
            i,j=x-c,y-c
            while i<x+c:
                arr[i*M+j]=1
                i+=1
            i,j=x-c,y+c
            while i<x+c:
                arr[i*M+j]=1
                i+=1
    if t==4:
        #alternating columns filled entirely of same colour but in pieces of 2 blocks at a time
        #a star graph
        N,M=50,50
        arr=[j%2 for j in range(M)]*N
        for j in range(0,M,2):
            for i in range(0,N,3):
                arr[i*M+j]=0
    if t==5:
        N,M=50,50
        #boundary 1s rest 0s
        arr=[1]*M+ ( [1]+[0]*(M-2) +[1])*(N-2) +[1]*M
    if t==6:
        N,M=1,2
        arr=[0,1]
    if t==7:
        N,M=1,2
        arr=[0,0]
    if t>=8:
        N,M=50,50
        arr=[randint(0,1) for i in range(N*M)]
    print(N,M)
    for x in range(N):
        print(*[arr[x*M+y] for y in range(M)])