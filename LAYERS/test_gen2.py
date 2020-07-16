from random import *
seed(9749376976)
T=50
print(T)
for t in range(T):
    if t<=10:
        N=randint(10**3,5*10**3)
        C=100
        arr=[[2*randint(1,500),2*randint(1,500),randint(1,100)] for i in range(N)]
    if 11<=t<=20:
        N=randint(10**3,5*10**3)
        C=100
        arr=[[2*randint(1,50),2*randint(1,50),randint(1,100)] for i in range(N)]
    if 21<=t<=25:
        N=randint(10**3,5*10**3)
        C=100
        arr=[[2*randint(1,50),2*randint(1,50),randint(1,100)] for i in range(N)]
    if t>=26:
        N=randint(10,5*10**3)
        C=100
        arr=[[2*randint(1,5*10**8),2*randint(1,5*10**8),randint(1,100)] for i in range(N)]
    print(N,C)
    for w in arr:
        print(*w)
