def make_boundary(x,y,c,arr):
    i,j=x+c,y-c
    while j<y+c:
        arr[i*M+j]=1
        j+=1
    i,j=x-c,y-c
    while j<y+c:
        arr[i*M+j]=1
        j+=1
    i,j=x-c,y-c
    while i<=x+c:
        arr[i*M+j]=1
        i+=1
    i,j=x-c,y+c
    while i<=x+c:
        arr[i*M+j]=1
        i+=1

from random import *
T=10
for t in range(T):
    from random import *
seed(4598279840952759)
T=10
print(T)
for t in range(T):
    #4 squares inside a square, then 4 squares inside it, then......
    N,M=randint(45,50),randint(45,50)
    if t==0:
        N,M=50,50
        arr=[0]*(N*M)
        x,y=N//2,M//2
        c=23
        make_boundary(x,y,23,arr)
        coordinates=[(N//4,M//4),(3*N//4,3*M//4),(N//4,3*M//4),(3*N//4,M//4)]
        for s in range(4):
            make_boundary(coordinates[s][0],coordinates[s][1],8,arr)
            x,y=coordinates[s][0],coordinates[s][1]
            sign=[-1,1,1,-1]
            sign2=[1,1,-1,-1]
            for d in range(4):
                a,b=x+sign[d]*3,y+sign2[d]*3
                make_boundary(a,b,2,arr)
                arr[a*N+b]=1

    if t==1:
        arr=[0]*(N*M) 
        holes=randint(300,700)
        depth=7
        coordinates=[(N//4,M//4),(3*N//4,3*M//4),(N//4,3*M//4),(3*N//4,M//4)]
        for s in range(4):
            depth-=1
            x,y=coordinates[s]
            for c in range(1,2*depth,4):
                make_boundary(x,y,c,arr)
    if t==2:
        arr=[0]*(N*M) 
        holes=randint(300,700)
        depth=6
        coordinates=[(N//4,M//4),(3*N//4,3*M//4),(N//4,3*M//4),(3*N//4,M//4)]
        for s in range(4):
            depth-=1
            x,y=coordinates[s]
            for c in range(1,2*depth,3):
                make_boundary(x,y,c,arr)
    if t==3:
        #4 big nested holes of different depths from 5 to 2
        arr=[0]*(N*M) 
        holes=randint(300,700)
        depth=6
        coordinates=[(N//4,M//4),(3*N//4,3*M//4),(N//4,3*M//4),(3*N//4,M//4)]
        for s in range(4):
            depth-=1
            x,y=coordinates[s]
            for c in range(1,2*depth,2):
                make_boundary(x,y,c,arr)
    if t==4:
        #9 big nested holes
        arr=[1]*(M*N)
        coordinates=[]
        for x in range(3):
            for y in range(3):
                coordinates.append((N//6+x*(N//3),M//6+y*(M//3)))
        depth=3
        for s in range(9):
            x,y=coordinates[s]
            for c in range(1,2*depth,2):
                i,j=x+c,y-c
                while j<y+c:
                    arr[i*M+j]=0
                    j+=1
                i,j=x-c,y-c
                while j<y+c:
                    arr[i*M+j]=0
                    j+=1
                i,j=x-c,y-c
                while i<=x+c:
                    arr[i*M+j]=0
                    i+=1
                i,j=x-c,y+c
                while i<=x+c:
                    arr[i*M+j]=0
                    i+=1
    if t==5:
        #4 big holes
        arr=[0]*(N*M) 
        holes=randint(300,700)
        depth=5
        coordinates=[(N//4,M//4),(3*N//4,3*M//4),(N//4,3*M//4),(3*N//4,M//4)]
        for s in range(4):
            x,y=coordinates[s]
            for c in range(1,2*depth,2):
                make_boundary(x,y,c,arr)
    if t==6:
        #16 big nested holes
        arr=[1]*(M*N)
        coordinates=[]
        for x in range(4):
            for y in range(4):
                coordinates.append((N//8+x*(N//4),N//8+y*(N//4)))
        depth=3
        for s in range(16):
            x,y=coordinates[s]
            for c in range(1,2*depth,2):
                i,j=x+c,y-c
                while j<y+c:
                    arr[i*M+j]=0
                    j+=1
                i,j=x-c,y-c
                while j<y+c:
                    arr[i*M+j]=0
                    j+=1
                i,j=x-c,y-c
                while i<=x+c:
                    arr[i*M+j]=0
                    i+=1
                i,j=x-c,y+c
                while i<=x+c:
                    arr[i*M+j]=0
                    i+=1
        
    if t==7:
        #holes in depth 1 to 3
        arr=[0]*(N*M) 
        for d in range(1,4):
            s_holes=randint(1,5-d)
            if d>2:
                s_holes=1
            for s in range(s_holes):
                x,y=randint(2*d-1,N-2*d),randint(2*d-1,M-2*d)
                for c in range(1,2*d,2):
                    i,j=x+c,y-c
                    while j<y+c:
                        arr[i*M+j]=1
                        j+=1
                    i,j=x-c,y-c
                    while j<y+c:
                        arr[i*M+j]=1
                        j+=1
                    i,j=x-c,y-c
                    while i<=x+c:
                        arr[i*M+j]=1
                        i+=1
                    i,j=x-c,y+c
                    while i<=x+c:
                        arr[i*M+j]=1
                        i+=1 
    if t==8:
        arr=[0]*(N*M) 
        #spiral holes with depth=2
        s_holes=randint(6,8)
        for s in range(s_holes):
            x,y=randint(3,N-4),randint(3,M-4)
            for c in range(1,3+1,2):
                i,j=x+c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
                i,j=x-c,y+c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
        #spiral holes with depth=3
        s_holes=randint(4,5)
        for s in range(s_holes):
            x,y=randint(5,N-6),randint(5,M-6)
            for c in range(1,3+1,2):
                i,j=x+c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
                i,j=x-c,y+c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
    if t==9:
        #here we have holes of 
        #- 1 -
        #1 0 1
        #- 1 -
        arr=[0]*(N*M) 
        holes=randint(3,6)
        for i in range(holes):
            x,y=randint(2,N-1-2),randint(2,M-1-2)
            if x>0:
                arr[(x-1)*M+y]=1
            if y>0:
                arr[(x)*M+y-1]=1
            if x<N-1:
                arr[(x+1)*M+y]=1
            if y<M-1:
                arr[(x)*M+y+1]=1
        #L shaped holes
        holes1=randint(3,6)
        for i in range(holes1):
            x,y=randint(0,N-1),randint(0,M-1)
            l,b=randint(0,3),randint(0,3)
            for i in range(b):
                if (x-l)>=0:
                    arr[(x-i)*M + y]=1
            for j in range(l):
                if y-j>=0:
                    arr[x*M+y-j]=1
        #spiral holes with depth=2
        s_holes=randint(3,4)
        for s in range(s_holes):
            x,y=randint(3,N-4),randint(3,M-4)
            for c in range(1,3+1,2):
                i,j=x+c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
                i,j=x-c,y+c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
        #spiral hole with depth=6
        s_holes=randint(1,2)
        depth=6
        for s in range(s_holes):
            x,y=randint(2*depth-1,N-2*depth),randint(2*depth-1,M-2*depth)
            for c in range(1,2*depth,2):
                i,j=x+c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while j<y+c:
                    arr[i*M+j]=1
                    j+=1
                i,j=x-c,y-c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
                i,j=x-c,y+c
                while i<=x+c:
                    arr[i*M+j]=1
                    i+=1
    print(N,M)
    for e in range(N):
        print(*[arr[e*M+f] for f in range(M)])
