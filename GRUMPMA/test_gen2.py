from random import *
seed(893546395698405)
T=100
print(T)
for t in range(T):
    if t<=10:
        #N=K.....solution =1
        N=randint(1,10**4)
        K=N
        M=randint(max(1,K//99),100*K)
        arr=[i%M for i in range(1,N+1)]
    if 11<=t<=20:
        #N=K....solution =0 mostly
        N=randint(1,10**4)
        K=N
        M=randint(max(1,K//99),10*K)
        arr=[i%M for i in range(1,N)]
        arr+=[0]
    if 21<=t<=30:
        #decreasing array
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        arr=[i%M for i in range(N,0,-1)]
    if 31<=t<=40:
        #increasing in intervals of t-29
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        a=1
        arr=[a+(t-29)*i for i in range(0,N)]
    if 41<=t<=50:
        #decreasing in intervals of t-39
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        a=1
        arr=[1000000-(t-39)*i for i in range(0,N)]
    if t>=51:
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        arr=[randint(0,10**9) for i in range(N)]
    print(N,K,M)
    print(*arr)
