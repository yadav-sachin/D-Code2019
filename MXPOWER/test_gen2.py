from random import *
seed(749879574925)
T=100
print(T)
for t in range(T):
    N=randint(50,100)
    arr=[randint(-10**2,10**4) for i in range(N*N)]
    print(N)
    for i in range(0,N*N,N):
        print(*arr[i:i+N])