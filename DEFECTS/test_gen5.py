from random import *
seed(874957985745794735975)
T=10
print(T)
for t in range(T):
    N,M=randint(45,50),randint(45,50)
    if t==0:
        arr=[1]*(N*M)
        holes=randint(100,200)
        for r in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            arr[x*M + y]=0
    if t==1:
        arr=[1]*(N*M)
        holes=randint(1500,2000)
        for r in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            arr[x*M + y]=0 
    if t==2:
        arr=[1]*(N*M)
        holes=randint(45,75)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,4),randint(0,4)
            for i in range(b):
                if (x+i)<N:
                    arr[(x+i)*M + y]=0
            for j in range(l):
                if y+j<M:
                    arr[x*M+y+j]=0
    if t==3:
        arr=[1]*(N*M)
        holes=randint(900,1100)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,2),randint(0,2)
            for i in range(b):
                if (x+i)<N:
                    arr[(x+i)*M + y]=0
            for j in range(l):
                if y+j<M:
                    arr[x*M+y+j]=0
    if t==4:
        arr=[0]*(N*M) 
        holes=randint(100,150)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,2),randint(0,2)
            for i in range(b):
                if (x-l)>=0:
                    arr[(x-i)*M + y]=1
            for j in range(l):
                if y-j>=0:
                    arr[x*M+y-j]=1
    if t==5:
        arr=[0]*(N*M) 
        holes=randint(300,700)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,4),randint(0,4)
            for i in range(b):
                if (x-l)>=0:
                    arr[(x-i)*M + y]=1
            for j in range(l):
                if y-j>=0:
                    arr[x*M+y-j]=1
    if t==6:
        arr=[0]*(N*M) 
        holes1=randint(50,60)
        for i in range(holes1):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,4),randint(0,4)
            for i in range(b):
                if (x-l)>=0:
                    arr[(x-i)*M + y]=1
            for j in range(l):
                if y-j>=0:
                    arr[x*M+y-j]=1
        holes2=randint(50,60)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,4),randint(0,4)
            for i in range(b):
                if (x+i)<N:
                    arr[(x+i)*M + y]=0
            for j in range(l):
                if y+j<M:
                    arr[x*M+y+j]=0
    if t==7:
        arr=[0]*(N*M) 
        holes1=randint(15,30)
        for i in range(holes1):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,4),randint(0,4)
            for i in range(b):
                if (x-l)>=0:
                    arr[(x-i)*M + y]=1
            for j in range(l):
                if y-j>=0:
                    arr[x*M+y-j]=1
        holes2=randint(15,30)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,4),randint(0,4)
            for i in range(b):
                if (x+i)<N:
                    arr[(x+i)*M + y]=0
            for j in range(l):
                if y+j<M:
                    arr[x*M+y+j]=0
    if t==8:
        arr=[0]*(N*M) 
        holes=randint(900,1500)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            arr[x*M+y]=1
            if x>0:
                arr[(x-1)*M+y]=1
            if y>0:
                arr[(x)*M+y-1]=1
            if x<N-1:
                arr[(x+1)*M+y]=1
            if y<M-1:
                arr[(x)*M+y+1]=1
    if t==9:
        arr=[0]*(N*M) 
        holes=randint(60,80)
        for i in range(holes):
            x,y=randint(0,N-1),randint(0,M-1)
            arr[x*M+y]=1
            if x>0:
                arr[(x-1)*M+y]=1
            if y>0:
                arr[(x)*M+y-1]=1
            if x<N-1:
                arr[(x+1)*M+y]=1
            if y<M-1:
                arr[(x)*M+y+1]=1
    print(N,M)
    for e in range(N):
        print(*[arr[e*M+f] for f in range(M)])
