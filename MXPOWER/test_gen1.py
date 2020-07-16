from random import *
seed(824098609250714)
T=100
print(T)
for t in range(T):
    N=randint(1,100)
    arr=[randint(-10**5,10**5) for i in range(N*N)]
    print(N)
    for i in range(0,N*N,N):
        print(*arr[i:i+N])