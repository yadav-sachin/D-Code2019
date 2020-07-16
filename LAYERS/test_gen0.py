from random import *
seed(406850782860)
T=50
print(T)
for t in range(T):
    N=randint(10**2,5*10**3)
    C=randint(20,100)
    arr=[[2*randint(1,5*10**8),2*randint(1,5*10**8),randint(1,C)] for i in range(N)]
    if t==0:
        #single rectangle
        N=1
        C=1
        arr=[[2,2,1]]
    if t==1:
        #all rectangles of same dimensions
        N=10**3
        arr=[[10**6,10**6,randint(1,C)] for i in range(N)]
    if t==2:
        #all rectangles of same dimensions and same colour
        N=10**3
        arr=[[10**6,10**6,1] for i in range(N)]
    if t==3:
        #rectangles with increasing dimensions, changing colours
        N=10**3
        C=100
        arr=[[2*i+2,2*i+2,i%100+1] for i in range(N)]
    if t==4:
        #rectangles with decreasing dimensions, changing colours
        N=10**3
        C=100
        arr=[[10**8-2*i,10**8-2*i,i%100+1] for i in range(N)]
    if t==5:
        #rectangles with increasing dimensions, same colours
        N=10**3
        C=100
        arr=[[2*i+2,2*i+2,i%100+1] for i in range(N)]
    if t==6:
        #rectangles with decreasing dimensions, same colours
        N=10**3
        C=100
        arr=[[10**8-2*i,10**8-2*i,1] for i in range(N)]
    if t==7:
        #rectangles of increasing lenght, height same, changing colours
        N=10**3
        C=100
        arr=[[2*i+2,10**6,i%100+1] for i in range(N)]
    if t==8:
        #rectangles of increasing height, length same, changing colours
        N=10**3
        C=100
        arr=[[10**6,2*i+2,i%100+1] for i in range(N)]
    if t==9:
        #rectangles of increasing lenght, height same, same colours
        N=10**3
        C=100
        arr=[[2*i+2,10**5,1] for i in range(N)]
    if t==10:
        #rectangles of increasing height, length same, same colours
        N=10**3
        C=100
        arr=[[10**6,2*i+2,1] for i in range(N)]
    if t==11:
        #all rectangles of height=2, different colours
        N=10**3
        C=100
        arr=[[2*randint(1,5*10**8),2,randint(1,100)] for i in range(N)]
    if t==12:
        #all rectangles of lenght=2, different colours
        N=10**3
        C=100
        arr=[[2,2*randint(1,5*10**8),randint(1,100)] for i in range(N)]
    if t==13:
        #all rectangles are squares
        N=10**3
        C=100
        arr=[]
        for i in range(N):
            a=[2*randint(1,5*10**8)]*2 + [randint(1,100)] 
            arr.append(a)
    if t==14:
        #rectangles with decreasing dimensions, different colours...but the last rectangle is largest
        N=10**3
        C=100
        arr=[[10**8-2*i,10**8-2*i,randint(1,100)] for i in range(N-1)]
        arr=arr+[[10**9,10**9,1]]
    if t==15:
        #rectangles with increasing dimensions, ...but the last is smallest
        N=10**3
        C=100
        arr=[[2*i+10**4,2*i+10**4,randint(1,100)] for i in range(N-1)]
        arr=arr+[[2,2,100]]
    if t==16:
        #all rectangles of dimensions, 2*2
        N=10**3
        C=100
        arr=[[2,2,randint(1,100)] for i in range(N)]
    if t==17:
        #all rectangles of dimensions , 2*2 same colour
        N=10**2
        C=100
        arr=[[2,2,1] for i in range(N)]
    if t==18:
        #all rectangles of dimensions, 10**9 * 10**9
        N=10**3
        C=100
        arr=[[10**9,10**9,randint(1,100)] for i in range(N)]
    if t==19:
        #all rectangles of dimensions , 10**9 * 10**9 same colour
        N=10**3
        C=100
        arr=[[10**9,10**9,100] for i in range(N)]
    if t==20:
        #2 rectangles
        N=2
        C=2
        arr=[[42,64,1],[44,92,2]]
    if t==21:
        #2 rectangles
        N=2
        C=2
        arr=[[44,92,2],[42,64,1]]
    if t==22:
        #every pair of 5 rectangles same height, increasing lenght,....heights increasing
        N=10**3
        C=100
        arr=[]
        for i in range(N//5):
            for j in range(5):
                a=[10000*i+2, 10000*i+2*j+2,randint(1,100)]
                arr.append(a)
    if t==23:
        #every pair of 5 rectangles same height, decreasing lenghts,....heights decreasing
        N=10**3
        C=100
        arr=[]
        for i in range(N//5,0,-1):
            for j in range(5,0,-1):
                a=[10000*i+2, 10000*i+2*j+2,randint(1,100)]
                arr.append(a)
    print(N,C)
    for w in arr:
        print(*w)
