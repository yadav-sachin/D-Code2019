from random import *
seed(89247595729)
T=50
print(T)
for t in range(T):
    N=10**5//50
    C=100
    arr=[[2*randint(1,5*10**8),2*randint(1,5*10**8),randint(1,100)] for i in range(N)]
    print(N,C)
    for w in arr:
        print(*w)
