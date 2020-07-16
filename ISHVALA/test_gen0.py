from random import *
seed(9750975097)
T=6
print(T)
for t in range(T):
    N,M=randint(10,20), randint(10,20)
    X,Y=randint(1,N) , randint(1,M)
    s=randint(1,3)
    x, y = sample([ i for i in range(1,N+1)],X) , sample([ j for j in range(1,M+1)],Y)
    x.sort()
    y.sort()
    print(N, M)
    print(X,Y,s)
    if X:
        print(*x)
    if Y:
        print(*y)