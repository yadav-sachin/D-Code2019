from math import *
from random import *
seed(3987503950958)
T=100
print(T)
sign1=[-1,1,-1,1]
sign2=[1,1,-1,-1]
for t in range(100):
    N=randint(80,100)
    if t<=8:
        #type 1
        #4 pts on boundary
        x=-1*randint(1,100)
        arr=[x]*(N*N)
        y=randint(10**7,10**8)
        side=randint(30,N//2-1)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        pts=[]
        while(len(pts)<4):
            l=sign1[len(pts)%4]*randint(0,side)
            b=sign2[len(pts)%4]*(side-abs(l))
            if (x0+l)*N+y0+b not in pts:
                arr[(x0+l)*N+y0+b]=y
                pts.append((x0+l)*N+y0+b)
    if 9<=t<=14:
    #type 1
    #3 pts on diamond 
    #1 inside
        x=-1*randint(1,100)
        arr=[x]*(N*N)
        y=randint(10**7,10**8)
        side=randint(30,N//2-1)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        pts=[]
        while(len(pts)<3):
            l=sign1[len(pts)%4]*randint(0,side)
            b=sign2[len(pts)%4]*(side-abs(l))
            if (x0+l)*N+y0+b not in pts:
                arr[(x0+l)*N+y0+b]=y
                pts.append((x0+l)*N+y0+b)
        while(len(pts)<4):
            l=sign1[len(pts)%4]*randint(1,side-1)
            b=sign2[len(pts)%4]*randint(1,side-abs(l))
            if (x0+l)*N+y0+b not in pts:
                arr[(x0+l)*N+y0+b]=y
                pts.append((x0+l)*N+y0+b)
    if 16<=t<=25:
        #type 1
        x=-1*randint(1,100)
        arr=[x]*(N*N)
        y=randint(10**7,10**8)
        side=randint(2,10)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        pts=[]
        while(len(pts)<4):
            l=sign1[len(pts)%4]*randint(0,side)
            b=sign2[len(pts)%4]*(side-abs(l))
            if ((x0+l)*N+y0+b) not in pts:
                arr[(x0+l)*N+y0+b]=y
                pts.append((x0+l)*N+y0+b)
    if 26<=t<=35:
        arr=[choice([-1,1])*randint(0,100) for i in range(N*N)]
        banks=randint((N*N)//22,(N*N)//19)
        for i in range(banks):
            y=randint(0,N*N-1)
            arr[y]=randint(10**5,10**7)
    if 36<=t<=45:
        x=choice([-1,1])*randint(0,100)
        arr=[x for i in range(N*N)]
        side=randint(30,N//2-1)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        incr=randint(1,3)
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                arr[x*N+y]+=incr
    if 46<=t<=55:
        x=choice([-1,1])*randint(0,100)
        arr=[x for i in range(N*N)]
        side=randint(2,N//2-1)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        incr=randint(1,100)
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                arr[x*N+y]+=incr
    if 56<=t<=61:
        x=choice([-1,1])*randint(0,100)
        arr=[x for i in range(N*N)]
        side=randint(30,N//2-1)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        incr=randint(1,1000)
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                arr[x*N+y]+=incr
    if 61<=t<=67:
        x=choice([-1,1])*randint(0,100)
        arr=[x for i in range(N*N)]
        side=randint(2,N//2-1)
        x0,y0=randint(side,N-1-side),randint(side,N-1-side)
        incr=randint(1,10000)
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                arr[x*N+y]+=incr
    if 68<=t<=75:
        #the bigger diamond wins even without 4 larger values
        X=randint(1,10000)
        arr=[X]*(N*N)
        N=45
        arr[:N]=[-1*X]*N
        for j in range(N):
            arr[(N-1)*N+j]=-1*X
        for i in range(N):
            arr[i*N]=-1*X
        for i in range(N):
            arr[i*N+N-1]=-1*X
        side=21
        x0,y0=22,22
        sum_X=0
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                sum_X+=arr[x*N+y]
        side=randint(7,12)
        x1,y1=choice([(side+1,side+1),(side+1,45-2-side),(45-2-side,45-2-side),(45-2-side,side+1)])
        sum_Y=0
        for x in range(x1-side,x1+side+1):
            a=abs(abs(x1-x)-side)
            for y in range(y1-a,y1+a+1):
                sum_Y+=arr[x*N+y]
        sum_Y-=4*X
        Y=(sum_X-sum_Y)//4-10
        pts=[]
        while(len(pts)<4):
            l=sign1[len(pts)%4]*randint(0,side)
            b=sign2[len(pts)%4]*(side-abs(l))
            if (x1+l)*N+y1+b not in pts:
                arr[(x1+l)*N+y1+b]=Y
                pts.append((x1+l)*N+y1+b)
    if 76<=t<=85:
        #larger diamond wins with more value than small diamond
        X=randint(1,10000)
        arr=[X]*(N*N)
        N=45
        arr[:N]=[-1*X]*N
        for j in range(N):
            arr[(N-1)*N+j]=-1*X
        for i in range(N):
            arr[i*N]=-1*X
        for i in range(N):
            arr[i*N+N-1]=-1*X
        side=21
        x0,y0=22,22
        sum_X=0
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                sum_X+=arr[x*N+y]
        side=randint(7,12)
        x1,y1=choice([(side+1,side+1),(side+1,45-2-side),(45-2-side,45-2-side),(45-2-side,side+1)])
        sum_Y=0
        for x in range(x1-side,x1+side+1):
            a=abs(abs(x1-x)-side)
            for y in range(y1-a,y1+a+1):
                sum_Y+=arr[x*N+y]
        sum_Y-=4*X
        Y=(sum_X-sum_Y)//4-10
        l,b=side,0
        arr[(x1+l)*N+y1+b]=Y
        l,b=0,side
        arr[(x1+l)*N+y1+b]=Y
        l,b=-side,0
        arr[(x1+l)*N+y1+b]=Y
        l,b=0,-side
        arr[(x1+l)*N+y1+b]=Y
    if 86<=t<=93:
        #the smaller diamond wins here
        X=randint(1,10000)
        arr=[X]*(N*N)
        N=45
        arr[:N]=[-1*X]*N
        for j in range(N):
            arr[(N-1)*N+j]=-1*X
        for i in range(N):
            arr[i*N]=-1*X
        for i in range(N):
            arr[i*N+N-1]=-1*X
        side=21
        x0,y0=22,22
        sum_X=0
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                sum_X+=arr[x*N+y]
        side=randint(7,12)
        x1,y1=choice([(side+1,side+1),(side+1,45-2-side),(45-2-side,45-2-side),(45-2-side,side+1)])
        sum_Y=0
        for x in range(x1-side,x1+side+1):
            a=abs(abs(x1-x)-side)
            for y in range(y1-a,y1+a+1):
                sum_Y+=arr[x*N+y]
        sum_Y-=4*X
        Y=(sum_X-sum_Y)//4+200
        pts=[]
        while(len(pts)<4):
            l=sign1[len(pts)%4]*randint(0,side)
            b=sign2[len(pts)%4]*(side-abs(l))
            if (x1+l)*N+y1+b not in pts:
                arr[(x1+l)*N+y1+b]=Y
                pts.append((x1+l)*N+y1+b)
    if t>=94:
        #the smaller diamond wins here
        X=randint(1,10000)
        arr=[X]*(N*N)
        N=45
        arr[:N]=[-1*X]*N
        for j in range(N):
            arr[(N-1)*N+j]=-1*X
        for i in range(N):
            arr[i*N]=-1*X
        for i in range(N):
            arr[i*N+N-1]=-1*X
        side=21
        x0,y0=22,22
        sum_X=0
        for x in range(x0-side,x0+side+1):
            a=abs(abs(x0-x)-side)
            for y in range(y0-a,y0+a+1):
                sum_X+=arr[x*N+y]
        side=randint(7,12)
        x1,y1=choice([(side+1,side+1),(side+1,45-2-side),(45-2-side,45-2-side),(45-2-side,side+1)])
        sum_Y=0
        for x in range(x1-side,x1+side+1):
            a=abs(abs(x1-x)-side)
            for y in range(y1-a,y1+a+1):
                sum_Y+=arr[x*N+y]
        sum_Y-=4*X
        Y=(sum_X-sum_Y)//4+200
        l,b=side,0
        arr[(x1+l)*N+y1+b]=Y
        l,b=0,side
        arr[(x1+l)*N+y1+b]=Y
        l,b=-side,0
        arr[(x1+l)*N+y1+b]=Y
        l,b=0,-side
        arr[(x1+l)*N+y1+b]=Y
    print(N)
    for i in range(0,N*N,N):
        print(*arr[i:i+N])



    
        

