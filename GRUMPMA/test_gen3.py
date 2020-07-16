from random import *
seed(40586092842475)
T=100
print(T)
for t in range(T):
    if t<=20:
        #N=K.....solution =1
        N=randint(1,10**4)
        K=N
        M=randint(max(1,K//99),100*K)
        arr=[i%M for i in range(1,N+1)]
    if 21<=t<=40:
        #N=K....solution =0 mostly
        N=randint(1,10**4)
        K=N
        M=randint(max(1,K//99),10*K)
        arr=[i%M for i in range(1,N)]
        arr+=[0]
    if 41<=t<=60:
        #decreasing array
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        arr=[i%M for i in range(N,0,-1)]
    if 61<=t<=80:
        #increasing in intervals of t-60
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        a=1
        arr=[a+(t-60)*i for i in range(0,N)]
    if 81<=t:
        #decreasing in intervals of t-39
        N=randint(1,10**4)
        K=randint(1,1+N//100)
        M=randint(max(1,K//99),10*K)
        a=1
        arr=[100000000-(t-80)*i for i in range(0,N)]
    print(N,K,M)
    print(*arr)
