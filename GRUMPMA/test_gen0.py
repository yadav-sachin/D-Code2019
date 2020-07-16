from random import *
seed(472975927575)
T=100
print(T)
for t in range(T):
    N=randint(1,10**4)
    K=randint(1,N)
    M=randint(1,1000*K)
    if t==0:
        #M==1 ...nCk answer
        N=10000
        K=100
        M=1
    if t==1:
        #answer = no. of elements satisfying arr[i]%M==1
        N=10000
        K=1
        M=50
    if 2<=t<=12:
        #all elements are zero, 
        # M goes from 1 to 11
        N=10000
        M=t-1
        K=randint(M,10*M)
    if 13<=t<=16:
        #some more tests with M=1 ...nCk solution
        N=randint(20,5*10**3)
        K=randint(1,N//100)
        M=1
    if t==17:
        #N=1,K=1,M=1
        #solution =1
        N,K,M=1,1,1
    if 18<=t<=50:
        #M goes from 1 to 33
        N=randint(1,10**4)
        K=randint(1,1+N//500)
        M=t-17
    if 51<=t<=90:
        #K goes from 1 to 40
        N=randint(1,10**4)
        K=t-50
        if 51<=t<=70:
            M=100*K
        if 71<=t<=90:
            M=K//5+1
    arr=[randint(0,10**9) for i in range(N)]
    if t>90:
        #arr goes 0 1 2 3 4 .....M-1 0 1 2 3 4...... M-1 0 1 2 3.....M-1
        N=randint(10**3,10**4)
        K=N//100
        M=10
        arr=[ i%M for i in range(N)]
    print(N,K,M)
    print(*arr)
