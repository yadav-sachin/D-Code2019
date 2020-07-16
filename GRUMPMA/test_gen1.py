from random import *
seed(37935792370937)
T=100
print(T)
for t in range(T):
    if t<=5:
        #some random K,M for some N=10^4
        N=10000
        K=randint(10,N//100)
        M=randint(1,(K//10) +1)
    if 6<=t<=10:
        #M=1 cases
        N=randint(1000,10**4)
        K=randint(50,99)
        M=1
    if 11<=t<=15:
        #M=2 cases
        N=randint(1000,10**4)
        K=randint(10,N//100)
        M=max(2,K//5)
    if 16<=t<=20:
        #M=3 cases
        N=randint(1000,10**4)
        K=randint(100,N//10)
        M=max(3,K//25)
    if 21<=t<=25:
        #K=1 cases
        N=10000
        K=1
        M=randint(1,100)
    if 26<=t<=30:
        #K=2 cases
        N=10000
        K=2
        M=randint(1,100)
    if 31<=t<=35:
        #K=3 cases
        N=10000
        K=3
        M=randint(1,10)
    if 36<=t<=40:
        #K=N.........solution=0 highly likely
        N=10**4
        K=10**3
        M=randint(10,100)
    if 41<=t<=45:
        #K=1, M=1 ... solution =N
        N=randint(1,10**4)
        K=1
        M=1
    if t==46:
        #N=1, K=1, M=1
        N=1
        K=1
        M=1
    if t>=47:
        #go random
        N=randint(1,10000)
        K=randint(1,N)
        M=randint(100,120)
    arr=[randint(0,10**9) for i in range(N)]
    print(N,K,M) 
    print(*arr)