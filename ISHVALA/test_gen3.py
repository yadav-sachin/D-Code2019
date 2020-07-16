from random import *
seed(764027608)
T=100
print(T)
for t in range(T):
    N,M=randint(5*10**3, 10**4), randint(5*10**3, 10**4)
    X,Y=randint(0,N) , randint(0,M)
    s=randint(1,30)
    if 9<=t<=18:
        #s goes from min(m,n) to min(m,n)//10
        X,Y=randint(0,N//1000) , randint(0,M//1000)
        s=min(N,M)//(t-8)
    if t==19:
        #all rivers
        X,Y=N,M
    if t==20:
        #no rivers
        X,Y=0,0
    if 21<=t<=25:
        #no horizontal rivers
        Y=0
    if 26<=t<=30:
        #no vertical rivesrs
        X=0
    x, y = sample([ i for i in range(1,N+1)],X) , sample([ j for j in range(1,M+1)],Y)
    if 0<=t<=2:
        #alternate rivers
        s=1
        x=list(range(1,N+1,2))
        y=list(range(1,M+1,2))
        X,Y=len(x), len(y)
    if 3<=t<=5:
        #alternate rivers at distance of 2, s in [1,2,3]
        s=t-2
        x=list(range(1,N+1,3))
        y=list(range(1,M+1,3))
        X,Y=len(x), len(y)
    if 6<=t<=8:
        #alternate rivers at distance of 3, s in [2,3,4]
        s=t-4
        x=list(range(1,N+1,4))
        y=list(range(1,M+1,4))
        X,Y=len(x), len(y)     
    print(N, M)
    print(X,Y,s)
    x.sort()
    y.sort()
    if X:
        print(*x)
    if Y: 
        print(*y)