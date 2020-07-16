from random import *
seed(48028602868)
T=10
print(T)
for t in range(T):
    N,M=50,50
    arr=[0]+[i%2 for i in range(N*M)]
    start=randint(0,1)
    arr=arr[start:start+N*M]
    #few defects in a perfect chess board
    f_cnt=randint(5,10)
    for i in range(f_cnt):
        x,y=randint(0,49),randint(0,49)
        arr[x*50 + y]^=1
    print(N,M)
    for a in range(N):
        print(*[arr[a*M+b] for b in range(M)])