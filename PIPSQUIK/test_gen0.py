from random import *
seed(279474)
T=100
print(T)
for t in range(T):
    N, H=randint(1,1000), randint(2,1000)
    Y1, Y2 = randint(1,H-1) , randint(1,1000)
    L=randint(1,N)
    if 0<=t<=3:
        #solution=N or N-1 always
        L=N
    if 4<=t<=7:
        #solution = 0 or 1, with single obstacle and single life
        N=1
        L=1
    if 8<=t<=11:
        #passes all type 1 barriers
        Y1=H-1
    if 15<=t<=17 or t>=70:
        #1000 barriers count
        N=1000
    X=[ randint(1,1000) for i in range(N)]
    types=[ randint(1,2) for k in range(N)]
    if 47<=t<=48:
        #single obstacle and solution=0 always
        N=1
        L=1
        types=[1]
        X=[1]
        H=3
        Y1=1
    if 68<=t<=69:
        #single obstacle and solution=1 always
        N=1
        L=1
        types=[1]
        X=[5]
        H=2
        Y1=1
    if 12<=t<=14:
        #passes all the barriers touching them
        for z in range(N):
            if types[z]==1:
                X[z]=H-Y1
            else:
                X[z]=Y2
    if 15<=t<=18:
        #all type 1 barriers
        types=[ 1 ]*N
    if 19<=t<=22:
        #all type 2 barriers
        types=[ 2 ]*N
    if 23<=t<=25:
        #all obstacle of type 1 and passes touching them
        types=[ 1]*N
        X=[ H-Y1 ]*N
    if 26<=t<=29:
        #all obstacle of type 2 and passes touching them
        types=[ 2]*N
        X=[ Y2 ]*N
    if 30<=t<=32:
        #collides with all barriers 
        #solution=L-1
        for z in range(N):
            if types[z]==1:
                X[z]=H-Y1-1
            else:
                X[z]=Y2+1
    if 33<=t<=36:
        #passes all type 1, but hits most of type2
        H=2
        Y1=1
        Y2=1
    if 39<=t<=42:
        #hits most of type 1 obstacles, but passes most type2
        H=1000
        Y1=1
        Y2=1000
    if 43<=t<=46:
        # hits most of type 2 blocks and passes all type 1 blocks
        X=[ 1000 for a in range(N)]
    print(N, H, Y1, Y2, L)
    for j in range(N):
        print( types[j], X[j])