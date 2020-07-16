from random import *
seed(25902402884)
T=10
print(T)
for t in range(T):
    if t==0:
        #alternate colours on all board
        N, M=50, 50
        arr1=[i%2 for i in range(M)]
        arr2=[1]+arr1[0:M-1]
        arr=(arr1+arr2)*25
    if t==1:
        #already single colour, single unit board
        N,M=1,1
        arr=[0]
    if t==2:
        #single row, alternate blocks
        N, M =1, 50
        arr=[ i%2 for i in range(N*M)]
    if t==3:
        #upper_half 0s and lower half 1s
        N,M=2*randint(1,25), 2*randint(1,25)
        arr=[ 0 if i<(N*M)//2 else 1 for i in range(N*M)]
    if t==4:
        #left half 0s and right halsf 1s
        N,M=2*randint(1,25), 2*randint(1,25)
        arr=[ 0 if j<M//2 else 1 for j in range(M)]*N
    if t==5:
        #upper_half 0s and lower_halfs 0s with a 1s line in between
        N,M=randint(1,24), 2*randint(1,25)
        arr=[0]*(M*N) + [1]*M + [0]*(M*N)
        N=2*N+1
    if t==6:
        N,M=2*randint(1,25), randint(1,24)
        arr=[0]*M +[1]+[0]*M
        arr=arr*N
        M=2*M+1
    if t==7:
        #full row of same colour but alternating 000000 11111 000000 111111 00000
        N,M=50,50
        arr=([0]*50+[1]*50)*25
    if t==8:
        #full column of same colour but alternating
        N,M=50,50
        arr=[j%2 for j in range(M)]*N
    if t==9:
        #single column alternate blocks
        N,M=50,1
        arr=[ i%2 for i in range(N*M)]
    print(N,M)
    for x in range(N):
        print(*[arr[x*M+y] for y in range(M)])