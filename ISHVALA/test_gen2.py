from random import *
seed(8240958)
T=70
print(T)
for t in range(T):
    N,M=randint(10**3, 10**4), randint(10**3, 10**4)
    X,Y=randint(0,N) , randint(0,M)
    s=randint(2,10)
    if t<=10:
        #no vertical rivers
        X=0
    if 11<=t<20:
        #no horizontal rivers
        Y=0
    if 21<=t<=23:
        #no rivers
        X=0
        Y=0
        if t==23:
            #solution =1 with statue of size min(m,n)
            s=min(M,N)
    if 24<=t<=60:
        #statue side-length goes from 1 to 37
        s=t-23
    if 61<=t<=69:
        #statue size goes from min(n,m) to min(n,m)-8
        s=min(N,M)-69+t
    x, y = sample([ i for i in range(1,N+1)],X) , sample([ j for j in range(1,M+1)],Y)
    x.sort()
    y.sort()
    print(N, M)
    print(X,Y,s)
    if X:
        print(*x)
    if Y: 
        print(*y)