from random import *
seed(92498579578)
T=10
print(T)
for t in range(T):
    N,M=50,50
    arr=[randint(0,1) for i in range(N*M)]
    print(N,M)
    for x in range(N):
        print(*[arr[x*M+y] for y in range(M)])