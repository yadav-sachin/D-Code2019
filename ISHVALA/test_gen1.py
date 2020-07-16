from random import *
seed(792573076)
T=40
print(T)
for t in range(T):
    N,M=randint(100,200), randint(100,200)
    X,Y=randint(0,N) , randint(0,M)
    s=randint(2,5)
    if t<=2:
        #all board filled with water
        X,Y=N,M
    if 3<=t<=5:
        #no rivers
        X,Y=0,0
    if 6<=t<=8:
        #no vertical rivers
        X=0
    if 9<=t<=11:
        #no horizontal rivers
        Y=0
    x, y = sample([ i for i in range(1,N+1)],X) , sample([ j for j in range(1,M+1)],Y)
    if 12<=t<=14:
        #no horizontal river, only one vertical river
        Y=0
        y=[]
        X=1
        x=[ randint(1+1,N-1) ]
    if 15<=t<=18:
        #no vertical river, only one horizontal river
        Y=1
        y=[ randint(1+1,M-1)]
        X=0
        x=[]
    if t==19:
        #no vertical river, only one horizontal river at y=1
        Y=1
        y=[ 1]
        X=0
        x=[]
    if t==20:
        #no vertical river, only one horizontal river at y=N
        Y=1
        y=[M]
        X=0
        x=[]
    if t==21:
        #no horizontal river, only one vertical river at x=1
        Y=0
        y=[]
        X=1
        x=[1]
    if t==22:
        #no horizontal river, only one vertical river at x=M
        Y=0
        y=[]
        X=1
        x=[N]
    if t==23:
        #no vertical river, only two horizontal river at y=1,M
        Y=2
        y=[ 1,M]
        X=0
        x=[]
    if t==24:
        #no horizontal river, only two vertical river at x=1,N
        Y=0
        y=[]
        X=2
        x=[1,N]
    x.sort()
    y.sort()
    print(N, M)
    print(X,Y,s)
    if X:
        print(*x)
    if Y: 
        print(*y)