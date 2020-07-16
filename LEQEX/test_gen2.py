from random import *
seed(23809680262455)
T=5
print(T)
for t in range(T):
    N=10**5
    if t==0:
        #towers from height N//2 to 1
        N-=1
        arr=[1]*(N//2) + [2] + [1]*(N//2)
    if t==1:
        #trangles in alternate sequence
        arr=[i%30 +1 for i in range(N)]
    if t==2:
        #take all triangles
        N=3333*30 +1
        arr=[]
        for i in range(1,16,1):
            arr+=[i]*3333
        arr+=[1]
        for i in range(16,31,1):
            arr+=[i]*3333
    if t==3:
        #all triangles of same colour
        N-=1
        arr=[2]*N
    if t==4:
        #traingles in pairs
        arr=[]
        for i in range(N//2):
            arr+=[i%30 +1]*2
    print(N)
    arr=[randint(1,30) for i in range(N)]
    print(*arr)