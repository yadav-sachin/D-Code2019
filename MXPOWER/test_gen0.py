from random import *
seed(27495798603985026459)
T=100
print(T)
for t in range(T):
    if t==0:
        #single negative
        N=1
        arr=[-10**5]
    if t==1:
        #single max
        N=1
        arr=[10**5]
    if t==2:
        #single zero
        N=1
        arr=[0]
    if t==3:
        #full marrx
        N=100
        arr=[10**5]*(N*N)
    if t==4:
        #full negative
        N=100
        arr=[-10**5]*(N*N)
    if t==5:
        #full zero
        N=100
        arr=[0]*(N*N)
    if t==6:
        #full negative ...but one zero
        N=100
        arr=[-10**5]*(N*N)
        arr[(N//2)*(N//2)]=0
    if t==7:
        #full max ...but zero at border
        N=100
        arr=[10**5]*(N*N)
        for j in range(N):
            arr[j]=0
        for i in range(N):
            arr[i*(N)]=0
        for j in range(N):
            arr[(N-1)*N+j]=0
        for i in range(N):
            arr[i*(N)+N-1]=0
    if t==8:
        #full negative ...but zero at corners
        N=100
        arr=[-10**5]*(N*N)
        arr[0]=arr[N]=arr[(N-1)*N]=arr[N*N-1]=0
    if t==9:
        #N=2....arr= 01 10
        N=2
        arr=[0,1,1,0]
    if t==10:
        N=100
        arr=[-10**5]*(N*N)
        center=(N//2,N//2)
        arr[center[0]*N + center[1]]=0
    if t==11:
        N=100
        arr=arr=[-10**5]*(N*N)
        center=(N//2,N//2)
        arr[center[0]*N + center[1]]=arr[(center[0]+1)*N + center[1]]=arr[(center[0]-1)*N + center[1]]
    if 12<=t<=48:
        #all negative...except a single diamond of different size every time
        # make diamonds of different sizes
        N=100
        arr=arr=[-10**5]*(N*N)
        center=(N//2,N//2)
        arr[center[0]*N+center[1]]=10**5
        side=56-t
        for s in range(1,side+1,1):
            i=center[0]+s
            j=center[1]
            while( i >= center[0]):
                arr[i*N+j]=10**5
                i-=1
                j-=1
            i=center[0]
            j=center[0]-s
            while( j >= center[1]):
                arr[i*N+j]=10**5
                i-=1
                j+=1
            i=center[0]-s
            j=center[1]
            while(i <= center[0]):
                arr[i*N+j]=10**5
                i+=1
                j+=1
            i=center[0]
            j=center[1]+s
            while(j<=center[1]):
                arr[i*N+j]=10**5
                i+=1
                j-=1
    if t==49:
        #alternate positive negative
        N=99
        arr=[10**5 if i%2 else -10**5 for i in range(N*N)]
    if t>49:
        N=100
        arr=[randint(-10**5,10**5) for i in range(N*N)]
    print(N)
    for i in range(0,N*N,N):
        print(*arr[i:i+N])