from random import *
seed(2409570927527697)
T=100
print(T)
for t in range(T):
    N=randint(700,5000)
    if t==1:
        #single triangle
        N=1  
    arr=[randint(1,30) for i in range(N)]
    if t==2:
        #all triangles of same colour
        arr=[1 for i in range(N)]
    if t==3:
        #two triangles of same colour
        N=2
        arr=[1,1]
    if t==4:
        #30 triangles of different colours
        N=30
        arr=[i%30 +1 for i in range(N)]
    if t==5:
        #triangles of alternate colours
        arr=[j%2+1 for j in range(N)]
    if t==0:
        #palindrome array of size 59 [1 2 3 4 ...29 30 29 28 27.....4 3 2 1]
        N=59
        arr=[i for i in range(1,31)]
        arr=arr+list(range(29,0,-1))
    if t==6:
        #three triangles of 2 same and 1 different
        N=3
        arr=[2,1,1]
    #second test file content starts
    N=10**4
    arr=[randint(1,30) for i in range(N)]
    if t==7:
        #alternate 30 colour triangles from 1 to 30
        arr=[]
        for j in range(0,N):
            arr.append(j%30 +1)
    if t==8:
        #all same except one....different one at middle
        arr=[1 for j in range(N)]
        arr[N//2]=2
    if t==9:
        #all same except one....different one at start
        arr=[1 for j in range(N)]
        arr[0]=2
    if t==10:
        #all same except one....different one at end
        arr=[1 for j in range(N)]
        arr[N-1]=2
    N=randint(10**3,10**4)
    if 28<=t<=42:
        #Number of triangles go from 1 to 15
        N=t-27
    arr=[randint(1,30) for i in range(N)]
    if t==11:
        #same colour
        arr=[1 for j in range(N)]
    if t==12:
        #single triangle
        N=1
        arr=[1]
    if t==13:
        #two triangle different colour
        N=2
        arr=[1,2]
    if t==14:
        #two trianles of same colour
        N=2
        arr=[1,1]
    if t==15:
        #three triangles of same colour
        N=3
        arr=[1,1,1]
    if t==16:
        #three triangle of 2 same and 1 different
        N=3
        arr=[1,1,2]
    if t==17:
        #three triangle of 2 same and 1 different
        N=3
        arr=[1,2,1]
    if t==18:
        #three triangles of 2 same and 1 different
        N=3
        arr=[2,1,1]
    if t==19:
        #alternate triangles 1 2 1 2 1 2 1 2 ....
        arr=[j%2+1 for j in range(N)]
    if t==20:
        #alternate triangles 1 2 3 1 2 3 1 2 3 ....
        arr=[j%3+1 for j in range(N)]
    if t==21:
        #alternate triangles 1 2 3 4 1 2 3 4 1 2 3 4.....
        arr=[j%4+1 for j in range(N)]
    if t==22:
        #alternate triangles 1..30 1...30 1...30
        arr=[j%30+1 for j in range(N)]
    if t==23:
        #all same except one....different one at middle
        arr=[1 for j in range(N)]
        arr[N//2]=2
    if t==24:
        #all same except one....different one at start
        arr=[1 for j in range(N)]
        arr[0]=2
    if t==25:
        #all same except one....different one at end
        arr=[1 for j in range(N)]
        arr[N-1]=2
    if t==26:
        #first half all 111111 , second half 222222222
        arr=[1 for j in range(0,N//2)]
        arr=arr+ [2 for j in range(N//2,N)]
    if t==27:
        #first quarter 111111, second 222222, third 333333, fourth 444444
        arr=[ (j//(N//4))+1 for j in range(N)]
    if t>=43:
        N=randint(1,10000)
        arr=[randint(1,30) for i in range(N)]
    print(N)
    print(*arr)
